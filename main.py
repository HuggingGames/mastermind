"""Terminal version — no external dependencies."""
from game import new_game, play

def main():
    state, text = new_game()
    print(text)
    while not state.get('done'):
        try: cmd=input('> ').strip()
        except (KeyboardInterrupt,EOFError):
            print('\nÇıkılıyor.');break
        if cmd.lower() in ('quit','exit','çık'):
            break
        if cmd.lower() in ('reset','yeniden'):
            state,text=new_game()
        else:
            state,text=play(state,cmd)
        print(text)
if __name__=='__main__':main()
