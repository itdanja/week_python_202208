"""
    성적순으로 정렬
"""
def scoresort( ary ) :
    for i in range( 1 , len( ary) ) :
        for k in range( i , 0 , -1 ) :
            if ary[ k-1 ][1] < ary[k][1] :
                ary[k-1] , ary[k]  = ary[k] ,  ary[k-1]
    return ary

scoreAry = [ ['유재석' , 88 ] , ['강호동' , 99] ,
                     ['신동엽' , 71], ['하하' , 78]  ,
                     ['김희철' , 67] ,  ['김희철' , 92] ]

print('정렬 전 : ' , scoreAry )
scoreAry = scoresort( scoreAry )
print('정렬 후 : ' , scoreAry )



