---
title: "Fast intro to Hugo"
date: 2021-01-13T11:00:00-03:00
_build:
  list: never

url: /drafts/fast-hugo-intro
summary: If you are interested to learn about [Hugo](https://gohugo.io) but don't have
 time, this post is for you.
---

Starting with [Hugo](https://gohugoio.io), it's a bit difficult to know _what is what_.
Usually one first looks at some themes, then goes on to install Hugo and try out the 
[Quick start](https://gohugo.io/getting-started/quick-start/), and then go on to 
understand the logic of the [templating system](https://gohugo.io/templates/introduction).

That path is fine, but rather long. This is an attempt to condense all the essential 
information in 20 key points.

Because this article is for beginners to Hugo, some exceptions and special rules are omitted 
for the sake of clarity. See [Hugo docs](https://gohugo.io/documentation/) for the most precise 
and up-to-date explanations.

{{< toc >}}

## 1. Hugo is a static site generator
A static site is one which can be served from a static server. A static server's only 
job is to provide the necessary `*.html, *.js, *.css, etc` files to the clients.

In principle you can write those files by hand, but Hugo makes them easy to generate. 

## 2. Hugo is a CLI program
Hugo itself is an executable file with which you interact via the 
command line (PowerShell, cmd, bash). 

With Hugo installed, and with a Hugo project in the current directory, 
you can run `hugo`, which generates the site, or `hugo server`, which 
hosts the site in a local server so that you can see it in your browser. These are the two most important commands. 

The `-h` flag displays help for any given command.

Some familiarity with command line interface programs is needed. 

## 3. Hugo projects have a definite directory structure. 
The top level of a Hugo project may have these: 

{{< dir >}}
* \f config.yaml or config.toml or config.json
* \d archetypes
* \d assets
* \d config
* \d content
* \d data
* \d i18n
* \d layouts
* \d public
* \d resources
* \d static
{{</ dir >}}

Most are optional, but the configuration files are mandatory and are usually located at the top level (`config.yaml`). You can also write the config files in TOML and JSON.

`/public` is the default output directory: it is created to store the generated files.
It stands on its own: you can upload just those files to the static server and forget that you ever used Hugo to create them. 

## 4. Theme users edit configs and write in `/content`. 
If you just want to use a nice theme you saw at the [Hugo Themes Page](https://themes.gohugo.io/),
you can start with the example site (every theme has one) and then use your intuition to
edit the configuration files and add content files like the ones in the example.

In principle you can ignore the inner workings of the templating language and just write markdown, but somewhere along the line you'll need to know more. 

## 5. The generated site mirrors the structure of `/content`

If `/content` looks like this:

{{< dir >}}
* \d content 
  * \f _index.md
  * \d blog
    * \f _index.md
    * \f hello-world.md
    * \f bye-world.md
  * \d presentations
    * \f _index.md
    * \f why-hugo.md
    * \f why-go.md
    * \d math
      * \f _index.md
      * \f cuadratics.md
      * \f linearalgebra.md
{{</ dir >}}

The output in `/public` will be very similar:

{{< dir >}}
* \d public 
  * \f index.html
  * \d blog
    * \f index.html
    * \d hello-world
      * \f index.html
    * \d bye-world
      * \f index.html
  * \d presentations
    * \f index.html
    * \d why-hugo
      * \f index.html
    * \d why-go.md
      * \f index.html
    * \d math
      * \f index.html
      * \d cuadratics
        * \f index.html
      * \d linearalgebra
        * \f index.html
{{</ dir >}}

The site will look like this once it's hosted:

```none
https://example.com/
https://example.com/blog/
https://example.com/blog/hello-world/
https://example.com/blog/bye-world/
https://example.com/presentations/
https://example.com/presentations/why-hugo/
https://example.com/presentations/why-go/
https://example.com/presentations/math/
https://example.com/presentations/math/cuadratics/
https://example.com/presentations/math/linearalgebra/
```
Notice the correspondence between URL structure and `/content` structure.

## 6. `/content` contains markdown files that start with structured data

The first part of content files is called the "Front Matter", and is written in YAML, JSON, or TOML format. It stores metadata of the page, typically title, date, and others. Then, [Commonmark's flavor of markdown](https://commonmark.org) is used to write the text of the page.

Variables have various effects on the generated page. Some are Hugo-specific, and some are theme-specific. A big part of working with Hugo is figuring out what variables have to be set to do what you want. 

The following three versions of `/content/hello-world.md` have the same effect. Notice the different delimiters:

* YAML Front Matter
  ```
  ---
  title: Hello
  date: 2021-01-13T11:00:00-03:00
  ---
  Hello World!
  ```
* TOML Front Matter
  ```
  +++
  title = "Hello"
  date = "2021-01-13T11:00:00-03:00"
  +++
  Hello World!
  ```
* JSON Front Matter
  ```
  {
    title : "Hello",
    date : "2021-01-13T11:00:00-03:00"
  }
  Hello World!
  ```

## 7. `/layouts` contains the HTML templates.
Each page is rendered by inserting the variables and text from the content file into certain positions an HTML template. 
Out of the many templates located in `/layouts`, a specific one is selected for each page using a [wide set of rules](https://gohugo.io/templates/lookup-order). 

This is subset of rules I find convenient:

* `content/somepath/foo.md` will be rendered using `layouts/somepath/single.html`
* `content/somepath/_index.md` will be rendered using `layouts/somepath/list.html`.  
* `layouts/_default/single.html` and `layouts/_default/list.html` are used in the case that the others don't exist.

This way `/content`, `/layouts`, and `/public` will have similar structures.

## 8. Template writing means writing `HTML` sprinkled with `{{...}}`

Hugo's template language has types, variables, and functions, and it's borrowed from [Go Templates](https://pkg.go.dev/text/template/). 

Consider the following `layouts/_default/single.html` example:

```go-html-template
<html>
<head>
<title> {{ upper .Title }} </title>
</head>
<body> 
{{.Content}} 
</body>
```

When Hugo renders a page with this template, all the `{{ ... }}` clauses disappear, and some are replaced by the value of a variables or the result of a function. 

In the first clause, the `upper` function receives the `.Title` variable as an argument, which is a value of type `string` defined in the Front Matter. 

In the second clause, the variable `.Content` is inserted. In contains the markdown of the content file already rendered to HTML. This means that for example, `## Hello` turns into `<h2> Hello </h2>`. 

If this file was rendered: 
```none
---
title: Hello
---
## Hello World
```
 the generated file would look like this: 
```html
<html>
<head>
<title> HELLO </title>
</head>
<body> 
<h2> Hello World </h2>
</body>
```
Checkout the [documentation for `upper`](https://gohugo.io/functions/upper) and other functions if you are curious.

## 9. Hugo-specific variables depend on front matter, config, or position. 

The previous are examples of Hugo-specific Front Matter-defined variables. 

Some variables are available everywhere in the site (_global_ variables) like `.Site.Author`. This variable is defined in `config.yaml` as `author: John Doe` (remember that TOML and JSON also possible). 

Some variables, such as `.Pages`, are related to the position of the file in `/content`. 
`.Pages ` is available on all the `list.html` templates, and it contains an array of page objects 
of all the are children of that page. As an example, let's say that you website has a blog section
 at `www.example.com/blog`. You might want to put all the links to the posts so that the user can 
 navigate to them.

This is how: 
{{< dir >}}
* \f config.yaml
* \d content 
  * \f _index.md
  * \d blog 
    * \f _index.md
    * \f hello-world.md
    * \f bye-world.md
* \d layouts
  * \f index.html 
  * \d blog
    * \f single.html
    * \f list.html
      ```go-template-html
      <html>
      <head>
      <title> {{ .Title }} </title>
      </head>
      <body>
      Welcome to the blog! See the posts:
      <ol>
      {{ range .Pages }}
        <li>
        <a href="{{ .RelPermalink }}">{{ .Title }}</a>
        </li>
      {{ end }}
      <ol>
      </body>
      ```  
{{</ dir >}}

`range` is explained later, for now just look at the final result at `/public/blog/index.html`:

```html
<html>
<head> 
<title> Blog </title>
</head>
<body>
Welcome to the blog! See the posts:
<ol>
  <li>
   <a href="/hello-world">Hello World!</a>
  </li>
  <li>
   <a href="/bye-world">Bye World!</a>
  </li>
<ol>
</body>
```

## 10. User/Theme custom variables are accessed via `.Params`
`.Params` is a dictionary that stores all the variables that **don't** have a 
special meaning to Hugo.

This is an example for a Front Matter defined variable:

```
---
title: Hello
#..ect
my_custom_variable: "im a custom variable"
```
Using it in the template looks like: 

```go-html-template
<p> The value is: {{.Params.my_custom_variable}} </p>
```

Custom Site Variables are defined **as elements of the `params` object** inside `config.yaml`, not at the top level: 

```yaml
baseURL: https://example.com
#..etc
params: 
  my_custom_variable: "im a custom variable"
```
Then in any template:
```go-html-template
<p> The value is: {{.Site.Params.my_custom_variable}} </p>
```

## 11. The dot, `range` and `with` 

I didn't mention why the dot before `{{.Title}}` was included. The reason is that the dot contains the current context, or in other words, all the variables available at that moment. 

When a page is rendered, the `.` contains all the Page Variables as expected. However, that behavior changes when the statements like `range` and `with` _rebind_ the context. I used this in point #8 without explanation:

```
{{ range .Pages }}
  <li>
   <a href="{{ .RelPermalink }}">{{ .Title }}</a>
  </li>
{{ end }}
```
The `range` block iterates on the page objects of the section, in this case, the "blog" section.
Inside the range block, the dot means "in the context of the current iteration". 
As a result, `.Title` doesn't mean "the title of this page" as usual, but instead means
"the title of the **current iteration** page". 

To explain the `with` block I'll use a very common idiom: 

```go-template-html
{{ with .Params.my_custom_param }}
<p> The value is: {{.}} </p>
{{ end }}
```
The block is run if `.Params.my_custom_param` is set, and **not** run if it's missing. Within the block, the dot means "the `with` variable", in this case "my_custom_param".

## Things I could have said but I didn't 

I said before that this information is necessarily incomplete, so here I'll try to summarize for each section the parts that would be missing. 

1. Every client gets the same files: there's no server-side intelligence or interaction. 
Interaction is possible, but only using Javascript on the client-side.
2. 
3. * the output directory can be changed using the `publishDir` configuration variable: in `config.yaml`: `publishDir: docs`.
   * the configurations can live in `/config`, but the rules are a bit weird. [See the relevant docs](https://gohugo.io/getting-started/configuration/#configuration-directory)
4. 
5. This is a general rule. You can force the URLs to be different, which you can see in [the documentation of URL Management](https://gohugo.io/content-management/urls/). Also, the pages don't need to be contained in a single `.md`. There's another way to organize content files called [Page Bundles](https://gohugo.io/content-management/page-bundles/) which allows you to divide each page on a separate directory where you can also keep the images and resources specific to that page.
6. Files other than markdown can be used, including html, pandoc, etc. [See the list of content formats](https://gohugo.io/content-management/formats/#list-of-content-formats)
7. Again, many other structures are possible, it's a matter of preference. The one I chose to is the easiest to learn.
8. 
9.  For reference: [Complete List of Site Variables](https://gohugo.io/variables/site), [Complete List of Page Variables](https://gohugo.io/variables/page)
10. 
11. When the context has been rebinded, you loose access to all the Page variables and so on. In case you need them, then use the `$`. It's a variable that is set to the initial value of the dot. You'd use it like this: `$.Site.Title`. Too much for this article.