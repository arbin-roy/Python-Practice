import pyautogui as p

p.hotkey('win', '4')
if p.alert(text='Click only after VDI window has opened', title='VDI', button='OK'):
    p.write('aroy11')
    p.press('tab')
    p.write('enCryptedDat@200')
    p.press('enter')
if p.alert(text='Auth done?', title='2FA', button='OK'):
    p.write('3')
    p.press('enter')
TOTP = p.prompt(text='Enter the OTP', title='OTP', default='')
p.write(TOTP)
p.press('enter')
if p.alert(text='Auth done?', title='2FA', button='OK'):
    p.write('enCryptedDat@200')
    p.press('enter')
