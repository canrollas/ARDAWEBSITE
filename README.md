# Replica of can rollas website
### Features

- Basic html bootstrap design and python flask usage
- 8 html pages
- 1 python main file
- Responsive bootstrap design
- Usage of javascript
- Connected with local database file with used structed query language
- Includes settings of Vscode

### Which types of algorithms/patterns used in this basic project

## Get redirect post pattern

- Basic knowledge of internet protocol reqires get redirect post pattern to get rid of resubmit error
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/PostRedirectGet_DoubleSubmitSolution.png/350px-PostRedirectGet_DoubleSubmitSolution.png)

- Basically when back button pressed it can be annoying to resubmitting form.

#### POST/GET patterns with python knowledge

- Basic knowledge of get/post form is applied with sql database language
- Giving the basic idea of the algorithm with psudo-code

```flow
st=start:Mail registiration
op=operation: GET method with http 200
cond=condition: Successful Yes or No?
form=operation:Data Input and POST request with protocol 3xx
controller=condition:If data in database Yes or No?
redirect1=end:Error you have already submitted
redirect2=end:Congrats you submitted mail
crash=Internet protocol error

st->op->cond
cond(yes)->form
form->controller
controller(yes)->redirect1
controller(no)->redirect2
cond(no)->crash

```
#### Google drive pdf view iframe appended

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <p>Do not try the link it is empty<p>
    <body>
        <iframe src="https://drive.google.com" style="width:100%; height:600px; border:0;"></iframe>
    </body>
</html>
```
#### How to run the website
- just run the app.py after installation of flask etc.
#### Previews with pictures
- It will be on my domain in a few weeks

![](https://github.com/canrollas/Can-Rollas-Website/blob/main/image.png)
![](https://github.com/canrollas/Can-Rollas-Website/blob/main/image2.png)
![](https://github.com/canrollas/Can-Rollas-Website/blob/main/image3.png)

## Licence & copyright

© Can Rollas , Own website template

Lİcensed under the [Apache License](LICENSE).
