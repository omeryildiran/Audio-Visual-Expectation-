if targetPos[1]>0:
    if response.keys=='right':
        feedback="Doğru"
        Loop100.addData('Response', 1)
    elif response.keys=='left':
        feedback="Yanlış"
        Loop100.addData('Response', 0)
        
elif targetPos[1]<0:
    if response.keys=='left':
        feedback="Doğru"
        Loop100.addData('Response', 1)
    elif response.keys=='right':
        feedback="Yanlış"
        Loop100.addData('Response', 0)
        
           