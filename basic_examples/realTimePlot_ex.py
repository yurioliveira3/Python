
from drawnow import * #carrega a biblioteca drawnow
import matplotlib.gridspec as gridspec #carrega a biblioteca gridspec

#@brief: callable where the graphics are made
    def makeFig(self): 

        #Create the grid
        gs = gridspec.GridSpec(3, 3) #gridspec 3x3

        #Plot 1
        plt.subplot(gs[0, :])
        plt.title("Breathing Signal Window with GT Peaks ")
        plt.xlabel('Seconds')
        plt.ylabel('Normalized Amplitude')
        #We should use 1000 Hz in this axis because breathing was resampled
        axis = ( np.linspace(0, len(self.breathing)/1000, len(self.breathing), endpoint=True) )
        plt.plot(axis, self.breathing, label='BREATHING SIGNAL', color = 'black')

        ##In this axis we should use the video frequency, which is 59.94 FPS
        axis2 = ( np.linspace(0, len(self.resp_peaks)/59.94, len(self.resp_peaks), endpoint=True) )
        #I'm using the same len as the breathing signal
        #axis2 = ( np.linspace(0, len(self.breathing)/1000, len(self.resp_peaks), endpoint=True) )
        plt.plot(axis2, self.resp_peaks, label='GT PEAKS', color='orange')
        plt.legend(loc='upper right')


        #Plot 2
        plt.subplot(gs[1, :])
        plt.title('Breathing Signal')
        plt.grid(True)
        plt.plot(self.breathing)
        plt.axis('off')


        #Plot 3
        plt.subplot(gs[2,0])

        txt = '\nFrom       : '+str(round(self.it,2))+' s'
        txt+= '\nTo         : '+str(round(self.et,2))+' s'
        txt+= '\nRR         : '+str(round(self.current_rr,2))+ ' RPM'
        txt+= '\nMe RR      : '+str(round(self.mean_rr,2))+ ' RPM'
        txt+= '\nGT RR      : '+str(round(self.rr_gt,2))+ ' RPM'
        txt+= '\nMe GT RR   : '+str(round(self.mean_rr_gt,2))+ ' RPM'

        #txt = '\nFrom       : %.2f'%((round(self.it,2)))
        #txt+= '\nTo__       : %.2f'%((round(self.et,2)))

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        # place a text box in upper left in axes coords
        plt.text(0.05, 0.95, txt, fontsize=14, verticalalignment='top', bbox=props)
        plt.axis('off')

        #Plot 4
        plt.subplot(gs[2,1])
        plt.title('Respiration Rate Estimation')
        plt.grid(True)
        plt.xlabel('N° of Predictions')
        plt.ylabel('RPM')
        plt.plot(self.rr_list)
        plt.axhline(np.mean(self.rr_list), label='Mean', color='orange', linestyle='dashed', linewidth=2)
        plt.legend()

        #Plot 5
        plt.subplot(gs[2,2])
        plt.title('Respiration Rate GT')
        plt.grid(True)
        plt.xlabel('N° of GT ')
        plt.ylabel('RPM')
        plt.plot(self.rr_gt_list)
        plt.axhline(np.mean(self.rr_gt_list), label='Mean', color='orange', linestyle='dashed', linewidth=2)
        plt.legend()
#end

if __name__ == "__main__":
    drawnow(makeFig)
    #UPDATED TIME - I ADDED a delay in order to do a better visualization
    time.sleep(0.4)