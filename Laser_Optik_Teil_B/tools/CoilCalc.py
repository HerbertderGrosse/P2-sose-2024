import matplotlib.pyplot as plt
from scipy.special import ellipk, ellipe
from numpy import pi, sqrt
import numpy as np
import warnings
import time

warnings.filterwarnings("ignore", category=RuntimeWarning)

muh0 = 4E-7 * pi
uo = 1


def combined_b(i,a,x,y):
    Bo =  i*uo/2./a 
    al =  x/a
    be =  y/a
    ga =  y/x
    Q =  (1 + al)**2 + be**2   
    k =  sqrt(4*al/Q)      
    K =  ellipk(k**2.0)          
    E =  ellipe(k**2.0) 
    
    vor = Bo/pi/sqrt(Q) 

    x_comp = vor*ga*(E*((1.0+al**2+be**2)/(Q-4*al)) - K) 
    
    y_comp = vor*(E*((1.0-al**2-be**2)/(Q-4*al)) + K)
    
    return x_comp,y_comp


        
def Baxial(i, a, y, u=uo):

    return (u*i*a**2)/2.0/(a**2 + y**2)**(1.5)

     
            
            
class Spule:
    
    def __init__(self,wire_num,height=None,inner_diameter=None,outer_diamter=None):
        
        if isinstance(wire_num,int):
            self.timestart = time.time()
            self.wire_num = wire_num
            self.height = height
            self.di =inner_diameter
            self.do = outer_diamter
            self.create_wires()
            
            
        else:
            self.wire_x,self.wire_y = wire_num
            self.width = int(round(np.max(wire_num[1])*1.4))
            self.max = np.max(wire_num[0])
            self.min = np.max(-wire_num[1])
            self.height = self.max+self.min
            self.stepsize = height
            self.wire_num =self.wire_x.size
            
        if self.height<self.width:
            self.height = self.width
            
        if self.width*2 < self.height:
            self.width = int(round(self.height/2))
            
    


        
    
    def frame(self):
        self.ys = np.arange(0,self.height)
        self.xs = np.arange(1,self.width)
        self.grid = np.meshgrid(self.xs,self.ys)
        
        
    
    def create_wires(self):
        
        self.stepsize = sqrt((self.do-self.di)*self.height/self.wire_num/2)
        
        ri = int(round(self.di/2/self.stepsize))
        
        verticals = int(round(self.height/self.stepsize))
        
        row_number = self.wire_num//verticals
        
        rest = self.wire_num%verticals
        
        self.wire_x = np.array([])
        self.wire_y = np.array([])
        
        for element in range(row_number):
            self.wire_x = np.concatenate((self.wire_x,np.array([int(ri+element)]*verticals)))
            self.wire_y = np.concatenate((self.wire_y,np.arange(-round(verticals/2),verticals-round(verticals/2))))
        
        self.wire_x = np.concatenate((self.wire_x,np.array([ri+row_number]*rest)))
        self.wire_y = np.concatenate((self.wire_y,np.arange(-round(rest/2),rest-round(rest/2))))
            
            
        self.wire_x = self.wire_x.astype(int)
        self.wire_y = self.wire_y.astype(int)
        
        self.max = np.max(self.wire_y)
        self.min = np.max(-self.wire_y)
        self.height = self.max+self.min
        self.width = int(round(1.4*np.max(self.wire_x)))
        
    
        
        
        
        
    def add_core(self,ur,radius,low,high):
        
        print(np.max(self.field_c[1]))

        self.field_c[:,low+self.min+self.height:high+self.min+self.height,:radius] *= ur
        
        plt.plot([-radius,radius,radius,-radius,-radius],[low,low,high,high,low],color='brown',label='core',linewidth=2)
        
        print(np.max(self.field_c[1]))


                            
        
        
    def fields_dict(self):
        self.frame()
        '''
        Creates a list with all the possible fields of current wires in 2D-arrays
        '''

        self.dict_c = [0]*(self.width+1)
        
        for element in set(self.wire_x):
            
            #Upgrade
            C = combined_b(1,element,*self.grid)
            
            Bx,By = C
            
            field_of_wire_x = np.column_stack((np.zeros((self.height,1)),Bx))
            field_of_wire_y = np.column_stack((Baxial(1,element,self.ys),By))
            
            field_of_wire_x[0,element] = 0
            field_of_wire_y[0,element] = 0
            


            large_x = np.concatenate((field_of_wire_x,np.zeros((self.max,self.width))))
            large_y = np.concatenate((field_of_wire_y,np.zeros((self.max,self.width))))
            
            large_x_low = np.concatenate((field_of_wire_x,np.zeros((self.min,self.width))))
            large_y_low = np.concatenate((field_of_wire_y,np.zeros((self.min,self.width))))
            
            #print(field_of_wire_c.shape,field_of_wire_x.shape,field_of_wire_y.shape)
            
            #large_c = np.concatenate((field_of_wire_c,np.zeros((2,self.height-1,self.width))))

            
            x = np.concatenate((-np.flipud(large_x_low[1:]),large_x),axis=0)
            y = np.concatenate((np.flipud(large_y_low[1:]),large_y),axis=0)
            
            self.dict_c[element] = np.array([x,y])
            

            
        
    def field_c_direciton(self):
        '''
        complete field
        '''
        self.fields_dict()
        
        self.field_c = np.zeros((2,2*self.height-1+self.max+self.min,self.width))
        
        for x,y in zip(self.wire_x,self.wire_y):
            self.field_c += np.roll(self.dict_c[x],y,axis=1)
            
        self.field_c /= self.stepsize
            
            

            
    def inductivity(self):
        '''
        Calculates Inductivity of Coil
        '''
        self.field_c_direciton()
        
        area_array = self.stepsize**2*pi/4*np.array([1]+[(1+2*i)**2-(-1+2*i)**2 for i in range(1,self.width)])
        flux = area_array*self.field_c[1]
            
        self.induct = sum([np.sum(flux[y+self.height+self.min-1,:x]) for x,y in zip(self.wire_x,self.wire_y)])  
        
        #area = np.sum(area_array[:int(round(np.mean(self.wire_x)))])

        area = self.stepsize**2*(np.mean(self.wire_x)-1/2)**2*pi
        
        
        analytic = uo*self.wire_x.size**2*area/(self.height*self.stepsize)

        #print('Induktivität numerisch: ',self.induct)
        #print('Induktivität analytisch: ',analytic)
        #print(f'Abweichung: {(self.induct-analytic)/ana*100}%')
        
        return self.induct, analytic
        
        
    def bisection(self,height,zylinder=None):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        plt.title('Querschnitt bei y=0')

        # Create the mesh in polar coordinates and compute corresponding Z.
        field = self.field_c[1,round(1.5*self.height)+height]
        
        r = np.arange(field.size)
        p = np.linspace(0, 2*np.pi, field.size)
        R, P = np.meshgrid(r, p)


        Z = np.array([field]*field.size)


        # Express the mesh in the cartesian system.
        X, Y = R*np.cos(P), R*np.sin(P)

        # Plot the surface.
        ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
        
        if zylinder != None:
            x = zylinder * np.sin(p)
            y = zylinder * np.cos(p)
            z = np.linspace(0,np.max(field))
            a,z = np.meshgrid(p,z)
            ax.plot_surface(x,y,z,alpha=0.3)

        # Tweak the limits and add latex math labels.
        ax.set_xlabel(r'$r$')
        ax.set_ylabel(r'$r$')
        ax.set_zlabel(r'$B(T)$')
        plt.gcf().set_dpi(400)
        plt.show()
        
    

                        
            
    def plot(self):    
        self.inductivity()
        
        '''
        Plot the created field
        '''
        
        field_c = self.field_c[:,self.min:-self.max]

        flipped = np.array(list(np.flip(field_c,axis=2)[:,:,:-1]))
        flipped[0] *= (-1)
        plot_c = np.concatenate((flipped,field_c),axis=2)
        

        amplitude = np.hypot(*plot_c)
        
        self.stepsize *= 1000


        x,y = np.meshgrid(np.arange(plot_c.shape[2])-(self.width-1), np.arange(-self.height+1,self.height))
        x = x.astype(float)*self.stepsize
        y = y.astype(float)*self.stepsize

        subsample = int(round(sqrt(self.height*self.width/100)))
        X = x[::subsample, ::subsample]
        Y = y[::subsample, ::subsample]
        U = plot_c[0,::subsample, ::subsample]
        V = plot_c[1,::subsample, ::subsample]
        
        
        plt.quiver(X, Y, U, V,scale=20*np.max(amplitude),width=0.005,label=f'Induktivität: '+"{:.4e}".format(self.induct)+'Hall')
        plt.xlabel(r'$Radius\,[mm]$')
        plt.ylabel(r'$Höhe\,[mm]$')
        #plt.pcolormesh(x, y, amplitude)
        

        
        pg = 100/self.width
        
        plt.imshow(amplitude, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='viridis',label='Feldstärke')
        plt.colorbar()
        plt.scatter(self.wire_x*self.stepsize,self.wire_y*self.stepsize,s=pg,color='orange',alpha=0.5)
        plt.scatter(-self.wire_x*self.stepsize,self.wire_y*self.stepsize,s=pg,color='orange',alpha=0.5)
        self.stepsize /= 1000
        #plt.legend()
        
        plt.title(r'$Feldstärke\,[\frac{A}{m}]$')
        
        #plt.contour(x,y,amplitude)

        self.wire_length = sum([self.stepsize*x*2*pi for x in self.wire_x])

        textstr = '\n\n'.join((
            r'$Daten\,:$',
            r'$Induktivität\,[H] = %.4f$' % (self.induct*muh0, ),
            r'$Feldstärke(Mitte)\,[\frac{A}{m}] = %.2f$' % (self.field_c[1,self.height+self.min,0]/uo, ),
            r'$Windungszahl = %.0f$' % (round(self.wire_num,0), ),
            r'$Drahtlänge\,[m] = %.2f$' % (self.wire_length, ),
            r'$Drahtdurchmesser\,[mm] = %.2f$' % (self.stepsize*1000, ),
            r'$Widerstand\,[\Omega] = %.2f$' % (0.01678/(self.stepsize**2*pi*1000000/4)*self.wire_length, )))

        
        
        ax = plt.gca()
        axpos = ax.get_position()
        
        props = dict(facecolor='wheat', alpha=0.5)
        
        ax.text(axpos.x1 + 1, axpos.y1, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)
        
        #plt.text(axpos.x1 + 0.7, axpos.y1, 'Spulendaten', horizontalalignment='left', transform=ax.transAxes)
        #plt.text(axpos.x1 + 0.8, axpos.y1-0.1, 'Induktität:  '+"{:.3e}".format(self.induct)+' Henry', horizontalalignment='left', transform=ax.transAxes)
        #plt.text(axpos.x1 + 0.8, axpos.y1-0.15, 'Drahtlänge:  '+"{:.3e}".format(self.wire_length)+' meters', horizontalalignment='left', transform=ax.transAxes)
        #plt.text(axpos.x1 + 0.8, axpos.y1-0.2, 'Widerstand:  '+"{:.3e}".format(0.01678/(self.stepsize**2*pi*1000000/4)*self.wire_length)+' Ohm', horizontalalignment='left', transform=ax.transAxes)
        #plt.text(axpos.x1 + 0.8, axpos.y1-0.25, 'zentrales H-Feld:  '+"{:.3e}".format(self.field_c[1,self.height+self.min,0]/uo)+' V/m', horizontalalignment='left', transform=ax.transAxes)
        #plt.text(axpos.x1 + 0.8, axpos.y1-0.3, 'Windungszahl:  '+str(self.wire_num), horizontalalignment='left', transform=ax.transAxes)
        
        
        plt.gcf().set_dpi(400)
        
        plt.show()
        
        

    def plot3d(self):
        
        field_c = self.field_c[:,self.min:-self.max]

        x,y = np.meshgrid(np.arange(field_c.shape[2])-(self.width-1), np.arange(-self.height+1,self.height))
        x = x.astype(float)*self.stepsize
        y = y.astype(float)*self.stepsize
        
        ax = plt.figure().add_subplot(projection='3d')

        # Make the grid
        x, y, z = np.meshgrid(x,x,y)

        # Make the direction data for the arrows
        u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
        v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
        w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))

        ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)


        plt.show()

        
        