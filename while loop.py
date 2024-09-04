msg=input ('enter your first msg:')
input_msg=msg
while msg!='exit':
    msg = input ((f'your last msg was {input_msg} what next:'))
    input_msg = input_msg +' ' + msg
