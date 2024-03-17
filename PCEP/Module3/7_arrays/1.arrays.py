"""Welcome to the Arrays"""
print("Welcome to the Arrays")

'''ChessBoard'''
chessboard=[]

for i in range(8):
    rowChess=[]
    for place in range(8):
        rowChess.append(place)
    chessboard.append(rowChess)
print(chessboard)
print()