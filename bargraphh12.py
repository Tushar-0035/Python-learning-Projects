from matplotlib import pyplot as plt
players=["Dhoni","Raina","Virat","Jadeja","Sachin tendulkar"]
scores=[89,23,78,12,34]
plt.bar(players,scores,colour="green")
plt.title("score board graph")
plt.xlabel("players")
plt.ylabel("scores")
plt.show()