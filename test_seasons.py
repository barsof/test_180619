user_input = input('what is the name of month?')
sea = 'Current season is'
a = ['winter','spring','autumn','summer']
wi = ['january','december','february', 1, 12, 02]
sp = ['march','april','may', 3, 4, 5]
su = ['june','jule','august', 6, 7, 8]
au = ['september', 'october', 'november', 9, 10, 11]



def month_qwi():
    if user_input in wi:
        print sea, a[0]
    elif user_input in sp:
        print sea, a[1]
    elif user_input in au:
        print sea, a[2]
    elif user_input in su:
        print sea, a[3]


month_qwi()

