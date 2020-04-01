import time


range_low= int(input("from which number do you want to check?: "))
range_high= int(input("until which number do you want to check?: "))

while range_low > range_high:
    print("sorry, the range has not entered properly \nlet's try again")
    time.sleep(1.5)
    range_low = int(input("from which number do you want to check?: "))
    range_high = int(input("until which number do you want to check?: "))




for i in range(range_low,range_high):
        original_num = i

        num_root= int(original_num**0.5)+1          #find root of the original number

        for z in range(1,num_root):

            if original_num %num_root !=0:       #check if the original number divide any number
                num_root= num_root-1

                if num_root==1:                  # means that the original number had divided only for 1
                    print ("prime number: {}".format(original_num))       # print the prime number number
                    break

                else:
                    continue






