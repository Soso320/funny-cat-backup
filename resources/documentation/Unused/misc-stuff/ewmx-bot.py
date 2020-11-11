import discord
from discord.ext import commands
import base64
from time import sleep

# don't worry about this part :trorr:

TOKEN = ('NzQ0Mjg2MzAzMzY0ODQxNTA1.XzhAog.OUNDrnf0THQseopKPCeoZ6cMyiY')

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("client ready")
@bot.command()
async def aqua(ctx):
    await ctx.send(":heart:")


@bot.command()
async def pecorine(ctx):
    if "a" in ctx.content or "b" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")



    if "c" in ctx.content or "d" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    if "a" in ctx.content or "b" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    if "e" in ctx.content or "f" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    if "g" in ctx.content or "h" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    if "i" in ctx.content or "j" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    if "k" in ctx.content or "l" in ctx.content:
        b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

        b64_bytes = b64_msg.encode('ascii')
        msg_bytes = base64.b64decode(b64_bytes)
        msgg = msg_bytes.decode('ascii')

        for i in range(1500):
            a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
            b = a * 100000
            print(b)
            samplestring = "abcdefghijkolprsqtcyxzwu"
            if "a" in samplestring:
                if "b" in samplestring:
                    if "z" in samplestring:
                        if "c" in samplestring:
                            if "d" in samplestring:
                                if "e" in samplestring:
                                    if "f" in samplestring:
                                        if "g" in samplestring:
                                            if "h" in samplestring:
                                                if "j" in samplestring:
                                                    if "k" in samplestring:
                                                        if "m" in samplestring:
                                                            if "n" in samplestring:
                                                                if "o" in samplestring:
                                                                    if "q" in samplestring:
                                                                        if "r" in samplestring:
                                                                            if "s" in samplestring:
                                                                                if "t" in samplestring:
                                                                                    if "u" in samplestring:
                                                                                        if "v" in samplestring:
                                                                                            if "w" in samplestring:
                                                                                                if "x" in samplestring:
                                                                                                    if "f" in samplestring:
                                                                                                        #further documentation needed
                                                                                                        # print("deez nuts")
                                                                                                        print("samplestring check done")
        sleep(5)
        for i in range(10):
            await ctx.send(msgg)

        for i in range(100):
            print(f"{i} {msgg}")

    else:
        if ctx.author.id not in {000000000000}:
                b64_msg = 'SSBIQVRFIHBlY29yaW5lIFNPIEZVQ0tJTkcgTVVDSEhISEhoIERVTUIgRlVDS0lORyBDSElORVNFIE5JR0dFUiBIT0Ug5oiR55yf55qE5b6I5Zac5qyiR2Vuc2hpbiBJbXBhY3Qg6L+Z5piv5LiA5Liq5Zug5Zac5Ymn5pWI5p6c6ICM5Lqn55Sf55qE5qih5Zug44CC5oiR5LiN5pSv5oyBIEdsb3Jpb3VzIExlYWRlciBYaSBKaW5waW5nIOaIluS7luS9nOS4uuaAu+e7n+eahOS4vuWKqOOAguaIkeeOsOWcqOWwhue7p+e7reS9v+eUqOmaj+acuuacr+ivreadpeS9v+i/meS4quWPmOW+l+aciei2o+OAggrlpKflnZflpLTlpKflnZflpLTlpKfnlLflrankuJzmlrnkvKDor7TkuaDov5HlubMgMTk4OSBNYXNzYWNyZSDlhajog73lpKfkuLvkuaDov5HlubPkuLvluK3msLjmgZIgVGhlIFhpbmppYW5nIFV5Z2h1ciBBdXRvbm9tb3VzIFJlZ2lvbiDotZ7nvo7liqDotJ3Ct+e6vee7tOWwlOWLi+eIteS4uuWPjeWHu+WSjOS/neWNq+WPpOS6uiBLdW5nLUZsdSDmiJDlkInmgJ3msZfmsqHlgZrplJnkuovvvIzkuaDov5HlubPlm73njovnu53mnYDkuobkvKDor7TkuK3nmoTmlYXkuosgVGhlIEdyZWF0IExlYXAgRm9yd2FyZA=='

                b64_bytes = b64_msg.encode('ascii')
                msg_bytes = base64.b64decode(b64_bytes)
                msgg = msg_bytes.decode('ascii')

                for i in range(1500):
                    a = 5 + 5 + 15819 + 1485918 + 1202314564 + 161819 * 15618981 + 18591891978941 * 5161548765343 - 18591891978941
                    b = a * 100000
                    print(b)
                    samplestring = "abcdefghijkolprsqtcyxzwu"
                    if "a" in samplestring:
                        if "b" in samplestring:
                            if "z" in samplestring:
                                if "c" in samplestring:
                                    if "d" in samplestring:
                                        if "e" in samplestring:
                                            if "f" in samplestring:
                                                if "g" in samplestring:
                                                    if "h" in samplestring:
                                                        if "j" in samplestring:
                                                            if "k" in samplestring:
                                                                if "m" in samplestring:
                                                                    if "n" in samplestring:
                                                                        if "o" in samplestring:
                                                                            if "q" in samplestring:
                                                                                if "r" in samplestring:
                                                                                    if "s" in samplestring:
                                                                                        if "t" in samplestring:
                                                                                            if "u" in samplestring:
                                                                                                if "v" in samplestring:
                                                                                                    if "w" in samplestring:
                                                                                                        if "x" in samplestring:
                                                                                                            if "f" in samplestring:
                                                                                                                #further documentation needed
                                                                                                                # print("deez nuts")
                                                                                                                print("samplestring check done")
                sleep(5)
                for i in range(10):
                    await ctx.send(msgg)

                for i in range(100):
                    print(f"{i} {msgg}")
        else:
            print("critical error")
            return


bot.run(TOKEN)
