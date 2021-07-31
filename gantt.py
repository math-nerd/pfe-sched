import time
import plotly as py
import plotly.figure_factory as ff
from solution import solution
from product import product
from jssp_instance import instance
import random

month_list = ["Janvier", 'Février', "Mars", "Avril", 'Mai', "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def gantt_chart(sol, month):
    n_start_time = []
    for i in range(sol.inst.L):
        for j in range(sol.inst.mfab):
            n_start_time.append(sol.FT[i][j])
        n_start_time.append(sol.CT[i])

    n_duration_time = []
    for i in range(sol.inst.L):
        for j in range(sol.inst.mfab):
            n_duration_time.append(sum([sol.inst.b[p][i]*sol.inst.times[p][j] for p in range(sol.inst.n)]))
        n_duration_time.append(sum([sol.inst.b[p][i]*sol.inst.pc[p] for p in range(sol.inst.n)]))


    n_bay_start = []
    for i in range(sol.inst.L):
        for j in range(sol.inst.mfab):
            n_bay_start.append(j)
        n_bay_start.append(sum([sol.X[i][a] * (a+sol.inst.mfab) for a in range(sol.inst.lin)]))


    n_job_id =[]
    for l in range(sol.inst.L):
        for i in range(sol.inst.mfab + 1):
            n_job_id.append(str(l+1))

    op =[]
    for l in range(sol.inst.L):
        op.append(str(l+1))
    
    colors=()
    col=['rgb(46, 137, 205)',
        'rgb(114, 44, 121)',
        'rgb(198, 47, 105)',
        'rgb(58, 149, 136)',
        'rgb(107, 127, 135)',
        'rgb(46, 180, 50)']

    for i in range(sol.inst.n):
        k =sum(sol.inst.lots[p] for p in range(i)) # le nombre de lot AVANT ce produit
        for l in range(k, k + sol.inst.lots[i]):
            colors = colors + (col[i],)
    """
    colors = ('rgb(46, 137, 205)',
            'rgb(114, 44, 121)',
            'rgb(198, 47, 105)',
            'rgb(58, 149, 136)',
            'rgb(107, 127, 135)',
            'rgb(46, 180, 50)')
    """
    #millis_seconds_per_minutes = 1000 * 60
    second_per_hour = 60*60*1000
    start_time= time.time() * 1000
    job_sumary = {}
    # Get the first process corresponding to the workpiece
    def get_op_num(job_num):
        index = job_sumary.get(str(job_num))
        new_index = 1
        if index:
            new_index = index + 1
        job_sumary[str(job_num)] = new_index
        return new_index

    def create_draw_defination():
        df = []
        for index in range(len(n_job_id)):
            operation = {}
            # Machine, ordinate
            if (n_bay_start.__getitem__(index) == 0):
                operation['Task'] = '1. Pesé et transfert de poudre'
            if (n_bay_start.__getitem__(index) == 1):
                operation['Task'] = '2. Mélangeur'    
            if (n_bay_start.__getitem__(index) == 2):
                operation['Task'] = '3. Granulateur'
            if (n_bay_start.__getitem__(index) == 3):
                operation['Task'] = '4. Ligne de conditionnement 1 '
            if (n_bay_start.__getitem__(index) == 4):
                operation['Task'] = '5. Ligne de condionnement 2'
            #operation['Task'] = 'Mélangeur' + str(n_bay_start.__getitem__(index) + 1)
            operation['Start'] = start_time.__add__(n_start_time.__getitem__(index) * second_per_hour)
            operation['Finish'] = start_time.__add__(
                (n_start_time.__getitem__(index) + n_duration_time.__getitem__(index)) * second_per_hour)
            # Artifact,
            job_num = op.index(n_job_id.__getitem__(index)) + 1
            operation['Resource'] = 'Lot' + str(job_num)
            df.append(operation)
        df.sort(key=lambda x: x["Task"], reverse=True)
        return df


    def draw_prepare():
        df = create_draw_defination()
        return ff.create_gantt(df, colors=colors, index_col='Resource',
                            title='Ordonnancement pour la production des produits sachets pour le mois de ' + month_list[month], show_colorbar=False,
                            group_tasks=True, data=n_duration_time,
                            showgrid_x=True, showgrid_y=True)


    def add_annotations(fig):
        y_pos = 0
        for index in range(len(n_job_id)):
            # Machine, ordinate
            y_pos = n_bay_start.__getitem__(index)

            x_start = start_time.__add__(n_start_time.__getitem__(index) * second_per_hour)
            x_end = start_time.__add__(
                (n_start_time.__getitem__(index) + n_duration_time.__getitem__(index)) * second_per_hour)
            x_pos = (x_end - x_start) / 2 + x_start

            # Artifact,
            job_num = op.index(n_job_id.__getitem__(index)) + 1
            text = 'Lot' + str(job_num) + "," + str(get_op_num(job_num)) + "=" + str(n_duration_time.__getitem__(index))
            # text = 'T' + str(job_num) + str(get_op_num(job_num))
            text_font = dict(size=14, color='black')
            fig['layout']['annotations'] += tuple(
                [dict(x=x_pos, y=y_pos, text=text, textangle=0, showarrow=False, font=text_font)])


    def draw_fjssp_gantt():
        fig = draw_prepare()
        add_annotations(fig)
        py.offline.plot(fig, filename='fjssp-gantt-picture'+str(month))


    #if __name__ == '__main__':
    return draw_fjssp_gantt()
