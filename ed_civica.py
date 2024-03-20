import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv
mesi_n = []
media_temp = []
giorni_giacca = []
giorni_scuola = []
giorni_gioco = []
data_file = open("./grafico.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    mesi_n.append(int(row[0]))
    media_temp.append(float(row[1]))
    giorni_giacca.append(int(row[2]))
    giorni_scuola.append(int(row[3]))
    giorni_gioco.append(int(row[4]))
    
    
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(15,10))
fig.suptitle('Correlazione e casualità')

ax1.plot(mesi_n, media_temp, 'red', linewidth=5)
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temp media')
ax1.grid()

ax2.plot(mesi_n, giorni_giacca, 'green', linewidth=3)
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con la giacca')
ax2.grid()

ax3.plot(mesi_n, giorni_scuola, 'blue', linewidth=4)
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di scuola')
ax3.grid()

ax4.plot(mesi_n, giorni_gioco, 'yellow', linewidth=5)
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di gioco')
ax4.grid()
ax4.set_ylim([0, 40])


plt.show()

#per compito 1 dato temp media terra (ultimi 50/100 anni), per 2 una grandezza correlata e casuale al 1 + 3 slide (1 grafico con fondi, 2 )