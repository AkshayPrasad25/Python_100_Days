trs=""" ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/ \-
 \_/__________________________________________________________________\_/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \-/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/ \-
 \_/__________________________________________________________________\_/ """
print("WELCOME TO JUMANJI!!")
print(trs)
print("YOU MUST FIND THE JEWEL TO SAVE JUMANJI")
direc=input('You are being chased and you have three directions to go towards left or right or continue straight : ')
if direc=='left':
    inp=input('You have now come to a lake filled with alligators would you wish to swim or wait for a boat which is driven by a local? (swim/boat) :')
    if inp=='swim':
        print("You risked your life and the alligators got to you! GAME OVER")
    else:
        print("You have crossed the lake and reached near the mountain and at the peak lies the jewel but you have to choose one item to climb the mountain")
        mount1=input('Buy Grappling hook or buy a mountain climbers set?(mountclimb/grap) :')
        if mount1=='mountclimb':
            print("Congratulations You have saved JUMANJI!!")
        else:
            print("You were severely injured during the climb.. GAME OVER!")
elif direc=='straight':
    inp1=input('You have entered a forest and its late in the night would you wish to proceed or wait till sunrise? (sunrise/proceed) :')
    if inp1=='sunrise':
        mount2=input('You got through the forest and reached the other side of the moutain where is is very steep would you choose a mountain climber set or grappling hook?(mountc/grap) :')
        if mount2=='grap':
            print("Congratualtions you found the JEWEL! YOU HAVE SAVED JUMAJI!!")
        else:
            print('You couldnt climp the mountain and took a major fall GAME OVER')
else:
    print("You have walked into a trap of the people trying to kill you!! GAME OVER")