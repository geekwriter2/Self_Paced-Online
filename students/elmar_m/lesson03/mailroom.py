#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson03: Mailroom Exercise Part 1
'''

donors = {
    'bill' : [2000, 7.5, 950000],
    'steve' : [5.5, 234000, 928],
    'donald' : [657, 234, 28.57, 90456],
    'angie' : [2, 99, 297765, 47, 28346],
    'kim' : [38982, 66.23, 9856, 0.1],
    }
 
def mail(n, m):
    '''
    Create mail text.
    '''
    print('Dear {}, thank you very much for your donation of {} dollars.\n'.format(n, m))

def thankyou():
    '''
    Show list of known donors, add new donor to list, add new donation to donor 
    '''
    name = None
    while name != 'x':
        print('>> give me a donor name, or type "l" to see a list. Type "x" to exit.')
        name = input('>> ')
        if name == 'l':
            print(' '.join(donors.keys()))
        elif name == 'x':
            break
        elif name in donors.keys():
            print('>>', name, 'already in list')

            donation = input('>> please add current donation:\n>> ')
            donors[name].append(int(donation))
            print('>>', donation, 'added to donation list of', name, 'thank you.\n')

            mail(name, donation)

        elif not name in donors.keys():
            print('>>', name, 'not in list, adding it ')
            donors[name] = [] 

            donation = input('>> please add current donation:\n>> ')
            donors[name].append(int(donation))
            print('>>', donation, 'added to donation list of', name, 'thank you.\n')

            mail(name, donation)
           
    print('> Options: 1 == quit | 2 == thankyou | 3 == report')

def report():
    '''
    Show an overview of current donors and donations
    '''

    # get the highest number:
    sumlist = []
    for i in donors.keys():
        sumlist.append(sum(donors[i]))
    maxn = len(str(max(sumlist)))
    maxn += 2

    fstring = '{:<20} ' + '|' + '{:>' + str(maxn) + '} ' + '|' + '{:>9}' + '|' + '{:>20}' # OK
    
    # print header line:
    # print(fstring.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))  # ~OK
    print(fstring.format('Donor Name', 'Total', 'Num Gifts', 'Average Gift'))  
    print('-' * (maxn + 54)) # ~OK

    for i in donors.keys():
        # print('>>', i, 'donated:', donors[i])
        # print('{} $ {} {} $ {}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) ))
        # print('{:<20} {:=$20} {:>20} {:=20}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) ))     # fail
        # print('{:<20} $ {:=20} {:>20} {:=20}'.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) # OK
        print(fstring.format(i, sum(donors[i]), len(donors[i]),  sum(donors[i])//len(donors[i]) )) 


def main():
    answer = None
    print(
        '> Options: 1 == quit | 2 == thankyou | 3 == report'
        )
        
    while answer != 'quit' and answer != '1':
        answer = input('> ')

        if answer == 'thankyou' or answer == '2':
            thankyou()
        elif answer == 'report' or answer == '3':
            report()
        
        


if __name__ == '__main__':
    main()
