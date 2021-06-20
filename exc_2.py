team = [
    "praveen",
    "isvarna",
    "captain",
    "venhat",
    "ballu",
    "mathi",
    "anil",
    "janani",
    "hewitt"
]

def generate_teams(arr,size ):
    k=0

    for i in range(size,len(arr) +size, size):
        if i < len(arr):
            print(arr[k:i])

            k= k+size
        else:
            print(arr[k:])
            break


#  start:end

generate_teams(team,4)