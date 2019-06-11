command = ''
while command.lower() != 'quit':
    started = False
    while True:
        command = input('>>  ')
        if command == 'start':
            if started == False:
                print('Car Started')
                started = True
            else:
                print('car already started')
        elif command == 'stop':
            if started == False:
                print('car already stopped')

            else:
                print('Car Stopped')
                started = False
        elif command == 'help':
            print('''
               stop - stop the car
               start - start the car
               quit - quit''')
        elif command == 'quit':
            break
        else:
            print('I dont understand that')
