# Kendriya Vidyalay TC Data

These scripts are used to get the admission numbers for which the online TC is yet to be issue or ommited to issue.

There are two scripts:

1. Node JS script
2. Python script

You can use any script, it's all upto you.


## Requirements

#### **Prerequisites**
You should have at least a basic understanding of fundamental programming concepts and some experience with introductory [`Javascript`](https://developer.mozilla.org/en-US/docs/Web/JavaScript) or [`Python`](https://python.org). And the knowledge of [`Node JS`](https://nodejs.dev/) is an advantage.


#### **Installation**
Make sure you have the following installed. And the installation will be based on your preferences. If you choose to go with Node JS then install Node JS related requirements only and if you choose to go with Python then install Python related requirements only.

##### **Node JS related requirements:**
- Latest version of [Node.js](https://nodejs.org/en/)
- Latest version of [NPM (Node Package Manage)](https://www.npmjs.com/get-npm)


##### **Python related requirements:**
- Latest version of [Python](https://python.org)


##### **Other optional requirements:**
- Latest version of [git](https://git-scm.com/) (**This is optional. It requires only if you choose to clone project**)




### Getting Started

1. Either you can **clone** or **download** repository from GitHub.

   - Clone with HTTPS *(required [git](https://git-scm.com/) installed in your system)*

     ```shell
     git clone https://github.com/vishalnagda1/kvs-scripts.git
     ```

   - Clone with SSH *(required [git](https://git-scm.com/) installed in your system)*

     ```sh
     git clone git@github.com:vishalnagda1/kvs-scripts.git
     ```

   - [Download Zip](https://github.com/vishalnagda1/kvs-scripts/archive/master.zip)

2. Navigate to project directory in the terminal or command prompt.

   ```shell
   cd kvs-scripts
   ```

3. Install project dependencies [**`Only for Node JS Users`**]
   
   **Note:** This step is only for Node JS users, if you're using python skip this step.

   ```shell
   npm install
   ```

4. Run the Script

    - Node JS User

        ```shell
        npm start <url> <from> <range> <logTcData>
        ```
    - Python User

        ```shell
        python tc-data.py <url> <from> <range> <log_tc_data>
        ```
        - `url` - It is required, and is the base url of your KV School e.g.
            
            - Node JS
                ```shell
                npm start https://no2udaipur.kvs.ac.in/ 3045701
                ```

            - Python
                ```shell
                python tc-data.py https://no2udaipur.kvs.ac.in/ 3045701
                ```
        - `from` - It is required, and is the starting admission number e.g.
            
            - Node JS
                ```shell
                npm start https://no2udaipur.kvs.ac.in/ 3045701
                ```

            - Python
                ```shell
                python tc-data.py https://no2udaipur.kvs.ac.in/ 3045701
                ```
        - `range` - It is optional, and is like how many next admission numbers you want to process like 10 or 20. The default value is 1. e.g.

            - Node JS
                ```shell
                npm start https://no2udaipur.kvs.ac.in/ 3045701 10
                ```
            
            - Python
                ```shell
                python tc-data.py https://no2udaipur.kvs.ac.in/ 3045701 10
                ```
        
        - `logTcData` or `log_tc_data` - It is optional, and is a flag value where 1 means to print TC issued data of processed admisison number and 0 (zero) means to skip the logging TC issue data. The default value is 0. e.g.
            
            - Node js
                ```shell
                python tc-data.py https://no2udaipur.kvs.ac.in/ 3045701 10 1
                ```

            - Python
                ```shell
                python tc-data.py https://no2udaipur.kvs.ac.in/ 3045701 10 1
                ```

5. Admission Number File Output:

   - Both script will generate `admission-numbers.txt` file in the project directory. It contains all the admission number whose TCs are not yet issued or omitted to issue.



#### Contributing

1. Fork it ( https://github.com/vishalnagda1/kvs-scripts/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new pull request.
