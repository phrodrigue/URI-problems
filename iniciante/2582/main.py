musicas = [
  "PROXYCITY",
  "P.Y.N.G.",
  "DNSUEY!",
  "SERVERS",
  "HOST!",
  "CRIPTONIZE",
  "OFFLINE DAY",
  "SALT",
  "ANSWER!",
  "RAR?",
  "WIFI ANTENNAS"
]
n = int(input())
for i in range(n):
  
  print(musicas[sum([int(x) for x in input().split()])])