n = 742449129124467073921545687640895127535705902454369756401331
e = 3
c = 39207274348578481322317340648475596807303160111338236677373
p = 752708788837165590355094155871
q = 986369682585281993933185289261
print(bytes.fromhex(hex(pow(c, pow(e, -1, (p-1)*(q-1)), n))[2:]).decode())