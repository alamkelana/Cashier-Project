# Cashier-Project

## Background

This program was made as a simple cashier application that can be used at physical or online stores as daily cashier application. Like all the cashiers we know, the program needs to have the following functions:
1. Add item to the cart
  - Adding item to the cart including item details like total item and item price
2. Update the inputted item
  - If the user has mistakenly input the item(s) and item(s) details, they can change the inputted item(s) and the details
  - Contains updating item name, total item, and item price
3. Delete the inputted item
  - If the user changed their mind and want to delete the inputted item, they will have two choices of delete
  - These two types of deletes is deleting on certain item name or delete all item(s) that was inputted
4. Checking the cart
  - Show the inputted item(s) that is already in the cart, and showing the total price for the item(s) they have inputted
5. Check out the order
  - Show the total price of all inputted item(s), showing the discount the user will get based on the condition below, and then showing the discounted price
  - Discount condition:
    - User will get 5% discount for purchases above Rp 200000
    - User will get 8% discount for purchases above Rp 300000
    - User will get 10% discount for purchases above Rp 500000

## How  to run the program

1. Make sure all 3 .py file is in the same folder
2. Run main.py, make sure you use an IDE so you could enjoy the whole experience with colored text, and use the program as your daily cahier machine

## Test Case

1. The main menu will look like this

![image](https://user-images.githubusercontent.com/109506146/216633737-728336ca-6b96-48ac-89d1-424dabacbf0f.png)

2. If you choose 1, it will ask you to input an item and its details, type Y to add another item, and N to end the inputting menu

![image](https://user-images.githubusercontent.com/109506146/216634024-0d5dcda9-976f-40a7-8b42-a9f040fdbfd6.png)

3. Typing 4 will check you inputted order

![image](https://user-images.githubusercontent.com/109506146/216634664-54c73632-ff6c-4122-916c-e48e4ad99cdd.png)

4. If you input your order wrong, you can update it by typing 2 in the main menu, or delete it by typing 3 in the main menu. Don't worry, if you forgot what you
inputted before, it will show altogether your inputted item first

![image](https://user-images.githubusercontent.com/109506146/216635485-48b170f3-c095-487e-bd77-f97502c7ce92.png)

![image](https://user-images.githubusercontent.com/109506146/216635694-7ca5f4f6-32cf-43b6-b8e5-2828ee1d5e33.png)

5. You can also reset all the transaction by typing 3 and then choose the 2nd type of delete which is reset all transaction

![image](https://user-images.githubusercontent.com/109506146/216636149-24f8c847-c43e-4dbe-91e1-d8f859e72a4e.png)

6. If you're done with everything, you can type 5 to check out your order, it will show your total purchases, and show the discount you will get

![image](https://user-images.githubusercontent.com/109506146/216636497-299df3de-63f2-4efc-87a3-091a7ea77d6e.png)

