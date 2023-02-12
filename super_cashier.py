# -*- coding: utf-8 -*-
"""super_cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YdUQ29HiF0s8orCp4vZaGU5MYlRwj8pz
"""

import pandas as pd
import numpy as np
from tabulate import tabulate

class Transaction:
  """The class consists of cashier program methods"""

  # Initiate empty dictionary and assign to Dataframe
  cashier_dict = {"Item": [], "Quantity": [], "Price": []}
  df = pd.DataFrame(cashier_dict)

  def __init__(self):
    self.greeting = "My dear customer, happy shopping!"
  
  def add_item(self, item_name: str, item_quantity: int, item_price: float or int):
    """Function to add item_name, item_quantity, item_price into the attribute class data
        
    Args:
        item_name (str): item name
        item_quantity (int): item quantity
        item_price (float or int): price for each item
    
    Raises:
        TypeError:
            If parameter of item_name is not string
        TypeError:
            If parameter of item_quantity is not integer
        TypeError:
            If parameter of item_price is not float atau integer
    """
    # Check type of data parameter of item_name
    if type(item_name) != str:
      raise TypeError("Parameter of 'item_name' must be 'str' type")
    # Check type of data parameter of item_quantity
    elif type(item_quantity) != int:
      raise TypeError("Parameter of 'item_quantity' must be 'int' type")
    # Check type of data parameter of item_price
    elif type(item_price) != float and type(item_price) != int:
      raise TypeError("Parameter of 'item_price' must be 'float' or 'int' type")
    else:
      # Assign parameter into attribute class data
      self.df.loc[len(self.df)] = [item_name, item_quantity, item_price] 
      print("The item details you want to buy")
      print(f"Item Name     : {item_name}")
      print(f"Item Quantity : {item_quantity}")
      print(f"Price for each item: Rp. {item_price}")   

  def update_item_name(self, item_name: str, update_name: str):
    """Function to update item_name if item_name is contained in the attribute class data
    Args:
        item_name (str): old item name
        update_name (str): new item name
        
    Raises:
        ValueError:
          If item_name is not contained in the attribute class data
        TypeError:
          If parameter of item_name is not string
        TypeError:
          If parameter update_name is not string
    """
    # Create list of all items in attribute class data
    list_item = self.df["Item"].tolist()
    try:
        # Check parameter item_name in list_item
        if item_name not in list_item:
            raise ValueError
        else:
            # Check type of data parameter item_name
            if type(item_name) != str:
                raise TypeError("Parameter 'item_name' must be 'str' type")
            # Check type of data parameter update_name
            elif type(update_name) != str:
                raise TypeError("Parameter 'update_name' must be 'str' type")
            else:
                # Filter by item_name
                # assign update_name in attribute class data
                self.df.loc[self.df.Item == item_name, "Item"] = update_name
                print(f"You update {item_name} to {update_name}")

    except ValueError:
        print(f"Item {item_name} is not found in this transaction")

  def update_item_quantity(self, item_name: str, update_qty: int):
    """Function to update item_quantity if item_name is contained in the  attribute class data
    
    Args:
        item_name (str): Item name as keys to update item_quantity
        update_qty (int): Value of new item_quantity 
      
    Raises:
        ValueError:
          If item_name is not contained in the class data attribute 
        TypeError:
          If parameter item_name is not string
        TypeError:
          If parameter update_qty is not integer
    """

    # Create list of all item in attribute class data
    list_item = self.df["Item"].tolist()
    try:
        # Check parameter nama_item in list_nama_item
        if item_name not in list_item:
            raise ValueError
        else:
            # Check type of data parameter nama_item
            if type(item_name) != str:
                raise TypeError("Parameter 'item_name' must be 'str'")
            # Check type of data parameter update_jml_item
            elif type(update_qty) != int:
                raise TypeError("Parameter 'update_qty' must be 'int'")
            else:
                # Filter by item_name
                # assign update_qty in attribute class data
                self.df.loc[self.df.Item == item_name, "Item Quantity"] = update_qty
                print(f"You update quantity of {item_name} to be {update_qty}")

    except ValueError:
            print(f"Item {item_name} is not found in this transaction")

  def update_item_price(self, item_name: str, update_price: float or int):
      """Function to update price if item_name in the attribute class data
        
      Args:
          item_name (str): item name as keys to update price
          update_price (float / int): value new price
      
      Raises:
          ValueError:
                If item_name is not contained in to class data atribute
          TypeError:
                If parameter nama_item is not string
          TypeError:
                If parameter update_price is not integer or float
      """
      # Create list of all item in attribute class data
      list_item = self.df["Item"].tolist()
      try:
          # Check parameter item_name in list_item
          if item_name not in list_item:
              raise ValueError

          else:
              # Check type of data parameter nama_item
              if type(item_name) != str:
                    raise TypeError("Parameter 'item_name' must be 'str'")

              # Check type of data parameter update_price
              elif type(update_price) != float and type(update_price) != int:
                    raise TypeError("Parameter 'update_price' must be float/int")

              else:
                  # Filter by item_name
                  # assign update_price in attribute class data
                  self.df.loc[self.df.Item == item_name, "Price"] = update_price
                  print(f"You update price {item_name} to be {update_price}")

      except ValueError:
          print(f"Item {item_name} is not found in this transaction")

  def delete_item(self, item_name: str):
    """Function to delete on of item in the class data attribute
        
    Args:
          item_name (str): item_name which is deleted
      
    Raises:
          ValueError:
             If item_name is not found in the class data attribute
          TypeError:
             If parameter attribute is not string
    Returns:
          table : order tabel with active class data attribute 
    """

    # Create list of all item in attribute class data
    list_item = self.df["Item"].tolist()
    try:
         # Check parameter item_name in list_item
         if item_name not in list_item:
              raise ValueError

         else:
              # Check type of data parameter item_name
              if type(item_name) != str:
                  raise TypeError("Parameter 'item_name' must be 'str'")
              
              else:
                  # Show deleted item
                  print(f"You delete item {item_name} from transaction")
                  # Filter and drop by item_name
                  df = self.df.drop(self.df.index[self.df.Item == item_name],inplace=True)
                  # Assign and show table
                  table = tabulate(df, headers="keys", tablefmt="psql")

                  return print(table)

    except ValueError:
            print(f"Item {item_name} is not found in this transaction")

  def reset_transaction(self):
      """Function to delete all items in the class data attribute
      
      Returns:
            table: order empty table
      """

      # Show blank table
      print("All items success deleted!")

      # Drop index in attribute class data
      self.df.drop(self.df.index, inplace=True)

      # Create  and show table
      table = tabulate(self.df, headers="keys", tablefmt="psql")

      return print(table)

  def check_order(self):
      """Function to count and show total price 
      
      Returns:
            table: Tabel order with total price 
      """

      # Copy attribute class data
      output_data = self.df.copy()

      # Create new column
      output_data["TotalPrice"] = (output_data.Quantity * output_data.Price)
      # Create and show table
      table = tabulate(output_data, headers="keys", tablefmt="psql")

      return print(table)

  def total_price(self):
        """Function to count total transaksi with discount
        Returns:
            int : total transaction
        """
        # Copy attribute class data
        output_data = self.df.copy()
        # Create new column
        output_data["TotalPrice"] = (output_data.Quantity * output_data.Price)
        # Assign variable total payment
        total = np.sum(output_data.TotalPrice)

        # If total payment les than 200.000 get normal price
        if total >= 0 and total <= 200_000:
            return print(f"Your total transaction is Rp.{int(total)}")

        # if total paymen more than 200.000 and less than 300.000
        # Get 5 percent discount
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(
                f"Your total transaction is Rp.{int(total_belanja)}"
            )

        # if total paymen more than 300.000 and less than 500.000
        # Get 8 percent discount
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(
                f"Your total transaction is Rp.{int(total_belanja)}"
            )

        # if total paymen more than 500.000, get 10 percent discount
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(
                f"Your total transaction is Rp.{int(total_belanja)}"
            )

        else:
            return "Total payment can't be negative"

