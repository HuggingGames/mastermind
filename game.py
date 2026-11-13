"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

def new_game():
    code=''.join(random.sample('123456789',4))
    return {'code':code,'tries':0,'done':False},"4 farklı rakamdan (1-9) oluşan kodu bul. 8 deneme. Örnek: 1234"
def play(s,action):
    if s['done']:return reply(s,'Yeni oyun başlat.')
    a=action.strip()
    if len(a)!=4 or not a.isdigit() or '0' in a or len(set(a))!=4:return reply(s,'1-9 arası 4 farklı rakam yaz.')
    s['tries']+=1;exact=sum(x==y for x,y in zip(a,s['code']));present=sum(c in s['code'] for c in a)-exact
    msg=f"🎯 Yerinde: {exact}, yanlış yerde: {present} | Deneme {s['tries']}/8"
    if exact==4:return finish(s,'Kazandın! '+msg)
    if s['tries']==8:return finish(s,f"Kaybettin. Kod: {s['code']}. "+msg)
    return reply(s,msg)
