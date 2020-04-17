import json
import random
import os
if __name__ == '__main__':
    count=random.randrange(1,5)
    time=random.randrange(1,5)
    cus_rep=random.randrange(-5,5)
    col_rep=random.randrange(-5,5)
    f = open('plot.json')
    file_content = f.read()
    current = json.loads(file_content)
    while(current['isnt_last']):
        os.system('cls')
        print('Количество разработчиков: ', count, '\n', 'Время на разработку: ',time,'\n','Репутация у заказчика',cus_rep,'\n','Репутация у коллег',col_rep, sep='')
        print(current['text'])
        answ=int(input())
        chance=random.randrange(0,100)
        for item in current['children']:
            if(answ == item['answer'] and (count >= item['count_min'] and count <= item['count_max'])and (time >= item['time_min'] and time <= item['time_max'])and (cus_rep >= item['cus_rep_min'] and cus_rep <= item['cus_rep_max'])and (col_rep >= item['col_rep_min'] and col_rep <= item['col_rep_max'])and (chance >= item['chance_min'] and chance <= item['chance_max']) ):
                current = item
                current['count'] = count + current['delta_count']
                current['time'] = time + current['delta_time']
                current['cus_rep'] = cus_rep + current['delta_cus_rep']
                current['col_rep'] = col_rep + current['delta_col_rep']
                count = current['count']
                time = current['time']
                cus_rep = current['cus_rep']
                col_rep = current['col_rep']
                break
        if (not (time >= 0 and count > 0)):
            print('Вы не справились')
            print('Количество разработчиков: ', count, '\n', 'Время на разработку: ', time, '\n',
                  'Репутация у заказчика', cus_rep, '\n', 'Репутация у коллег', col_rep, sep='')
            pass
    if( (time >= 0 and count > 0)):
        print('Вы справились')
        print('Количество разработчиков: ', count, '\n', 'Время на разработку: ', time, '\n', 'Репутация у заказчика',
              cus_rep, '\n', 'Репутация у коллег', col_rep, sep='')
        pass
    else:
        print('Вы не справились')
        print('Количество разработчиков: ', count, '\n', 'Время на разработку: ', time, '\n', 'Репутация у заказчика',
              cus_rep, '\n', 'Репутация у коллег', col_rep, sep='')
        pass
