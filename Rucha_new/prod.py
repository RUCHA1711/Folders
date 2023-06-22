
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Initialize driver
driver = webdriver.Chrome(ChromeDriverManager().install())


def get_csv_data(filepath):
    """
    This will read your csv data and convert it into the dataframe
    You can access the dataframe data using,

        -> For our test.csv data:
            dataframe["name"]: Will return all the names
            -> Output: ["dress", "music"]
            dataframe["total_results"]: Will return all the results
            -> Output: [5, 5]


            Dataframe looks like:
        -----------------------------------
            index    name     total_results
            0       dress       5
            1       music       5
            2       watch       0
        -----------------------------------
        => Here 0, 1, 2 are indexes


        -> You can loop through the dataframe using as follow:

                for idx in dataframe.index:
                    print(dataframe.iloc[idx])

            - Here dataframe.index contains the row numbers i.e. [0, 1, 2] (for our test.csv file):

        -> 'iloc' takes integer location (0, 1, 2, etc) and returns corresponding row
            - For eg,
                dataframe.iloc[0] returns the first row data [dress, 5]
    """
    dataframe = pd.read_csv('/Users/tagline_145/Downloads/test.csv')
    return dataframe


def search_product(product_name):
    # Open the url
    driver.get("http://demo-store.seleniumacademy.com/")

    # Find the seach box on the browser
    search_field = driver.find_element_by_name("q")
    search_field.clear()

    # Sends the product name
    search_field.send_keys(product_name)

    # Search for the product
    search_field.submit()

    # Get all products by accessing <h2> tag, as product names are written in h2 header
    products = driver.find_elements(By.TAG_NAME, "h2")

    # Return all the products
    return products


def print_all_resultant_product_name(products):
    print(f"----------------- PRODUCTS -----------------")
    for product in products:
        print(product.text)


def search_all_products(filepath):
    # get_csv_data will return dataframe
    dataframe = get_csv_data(filepath)

    # Access dataframe data
    for idx in dataframe.index:
        row = dataframe.iloc[idx]

        # Search for the given name
        product_name = row["name"]
        print(
            f"\n\n<-------------------------- SEARCHING FOR {product_name} PRODUCT... -------------------------->"
        )
        products = search_product(product_name)
        # Print the name of the product
        print_all_resultant_product_name(products)
        time.sleep(2)

        # Check if total number of products are equals to the given number of products in the csv file
        if len(products) == row["total_results"]:
            print(f"TEST CASE PASSED FOR {product_name} PRODUCT! :)")
        else:
            print(f"TEST CASE FAILED FOR {product_name} PRODUCT! :(")

        print(
            f"<--------------------- SEARCHING COMPLETED FOR {product_name} PRODUCT... --------------------->"
        )


# Pass the filepath to the function, we have passed the 'test.csv' file
search_all_products("test.csv")


"""
Execution Process:
=> The program will execute as below

The program execution will start from the line 103 after 'driver' is initialized.

1. The function search_all_products() will be called
2. We have passed the filename in search_all_products("test.csv"), to use test.csv data for finding products
3. The program will call the search_all_products() function.

4. The 'filepath' argument of the search_all_products(filepath) (line 74) will have value,
    filepath = "test.csv" (Came from line 103)
5. filepath will pe passed to the get_csv_data(filepath) (line 76) function.
6. The get_csv_data(filepath) function will read the file at 'filepath' which is "test.csv" in our example and will convert the csv data into dataframe (line 43-44).

7. After creating dataframe, get_csv_data(filepath) returns that dataframe, so our code will comes to the line 76 again.
8. We have stored that returned dataframe into 'dataframe' variable (line 76).
9. The dataframe has all rows data. So we will access each row one by one using for loop.

10. At line 79, we run the for loop on dataframe index i.e [0, 1, 2, etc]. 0 position denotes first row, 1 denotes second row, and so on.
11. To access the row data, on line 80, we used dataframe.iloc[idx] (Give me the data of row at position 'idx')
12. Now search the product name and stores the products result in the 'products' variable (line 87-89).

13. Print the products name and check test case is passed or failed (line 92-95).
"""