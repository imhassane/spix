# SPIX

An automatic broken url finder.

#### Main goal
I'm writing this to help me replace all the broken url in a database I'm working on currently. Those url are
for examples youtube urls used in my project or images url. <br />
It helps me replacing them and keeping my database coherent with its data.

Feel free to use it or edit it as you want it for your project.

## Usage
To install it, clone this repository or download it.

##### Input file
The input file is a txt file containing all the urls to test. You can also add rows such as databases names, tables or 
table's ids. <br />

<table>
    <thead>
        <th>url</th>
        <th>table</th>
        <th>id</th>
    </thead>
    <tbody>
        <tr>
            <td>https://google.fr</td>
            <td>t_suggetions_sug</td>
            <td>12</td>
        </tr>
        <tr>
            <td>https://theoncebook.wordpress.com</td>
            <td>t_favorites_fav</td>
            <td>100</td>
        </tr>
        <tr>
            <td>https://not-an-url.com/hello.gif</td>
            <td>t_covers_cov</td>
            <td>5</td>
        </tr>
        <tr>
            <td>https://inc.api/martin.png</td>
            <td>t_covers_cov</td>
            <td>10</td>
        </tr>
    </tbody>
</table>

Let's suppose our txt file is organized this way and is name `test.txt`. The first column is required to be the url, then we can add the others
rows. The txt file should look like this one below:

```text
https://google.fr t_suggetions_sug 2
https://theoncebook.wordpress.com t_favorites_fav 100
https://not-an-url.com/hello.gif t_covers_cov 5
https://inc.api/martin.png t_covers_cov 10
```

### Getting the broken urls
To get the broken urls we have to run the `main.py` file with its arguments.
If no arguments are provided the default configuration will be used and the example above won't work
as we suppose by default there only should be urls. To get this example to work, we need to run the command below:

`python main.py --rows "table id" --input-address test.txt`

Here we are adding two new rows to the SPIX configuration and the result should be:

```text
SPIX Broken url finder
STEP 1/3: Getting the file content
STEP 2/3: Filtering broken urls
         waiting for threads to end...
STEP 3/3: Dumping results into the output file: result
2 brokens url found
Done. Check your output file to see the broken urls and eventually replace them
:) :)

```

I hope I helped you understanding it more. 😍😍