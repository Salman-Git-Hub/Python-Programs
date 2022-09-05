def check_card(card_number):
    card_number_list =  [int(i) for i in card_number] # convert string to list
    tmp_list = []
    for i in range(0, len(card_number)):
        if i%2 == 0: # digits at even position
            check_num = card_number_list[i] * 2
            if check_num > 9: 
                # if greater than 9 then add digits
                check_num_list = [int(i) for i in str(check_num)]
                new_num = sum(check_num_list)
                tmp_list.append(new_num)
            else:
                tmp_list.append(check_num)
        else:
            tmp_list.append(card_number_list[i])

    # add all digits obtained
    check_sum = str(sum(tmp_list))
    # if the sum endswith '0' then the given card is valid
    if check_sum.endswith("0"):
        print("Card is valid!")
    else:
        print("Invalid card!")


if __name__=="__main__":
    card_number = input("Enter the credit card number\n>>>")
    check_card(card_number)
