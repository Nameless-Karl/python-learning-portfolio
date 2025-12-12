blocks = int(input("Enter the number of blocks: "))

#blocks = int(input("Enter the number of blocks: "))   # Takes in number of bricks available

count = 0 # Counts the number of iteration, which will become our wall height
rem_blocks = blocks # Number of blocks available as we go
used_blocks = 0 # Number of blocks used
need_blocks = 1 # Number of blocks needed to go on
while rem_blocks >= need_blocks: # Loop if the available blocks are more than we need for the next phase
    used_blocks = need_blocks + 1 # Used blocks is 1 plus (The logic is wrong)
    # rem_blocks = rem_blocks - used_blocks
    rem_blocks = rem_blocks - need_blocks # Available blocks is available blocks minus the number of blocks needed for last phase 
    need_blocks += 1 # The number of blocks needed for next phase increases by 1
    count += 1 # Our wall grows linearly
print("The height of the pyramid: ", count)
# Write your code here.
#	
height = count
print("The height of the pyramid:", height)

