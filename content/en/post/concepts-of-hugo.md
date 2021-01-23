---
title: Concepts of Hugo
subtitle: a what-is-what introduction
date: 2021-01-13T11:00:00-03:00

aliases: /drafts/fast-hugo-intro
summary: Learn [Hugo](https://gohugo.io) efficiently! 90% of Hugo explained in less than 25 key points.
---

When you start with [Hugo](https://gohugo.io) _The world’s fastest framework for building websites_, 
it's difficult to make sense of all the new vocabulary and concepts. 

This article is an attempt to give Hugo beginners a _what is what_ introduction to Hugo that will 
make the rest of the learning experience easier. 
The objective is to explain 90% of how Hugo works in less than 25 key points.

Clarity is prioritized over precision, so always refer to the official [Hugo Docs](https://gohugo.io/documentation) 
for the most precise and up-to-date information.

All the examples were tested at [`github.com/acanalis/concepts-of-hugo`](https://github.com/acanalis/concepts-of-Hugo).
If you want to give feedback, [message me at the Hugo Discourse!](http://discourse.gohugo.io/new-message?username=acanalis)

{{< toc >}}

# 1. Info for Everyone

## 1.1. Hugo is a static site generator
A static site is one which can be served from a static server. The only job of a static server
is to provide the necessary files `*.html, *.js, *.css, etc`  to the clients.

Every client gets the same files: there's no server-side intelligence or interaction.
Interaction is possible, but using JavaScript on the client-side.

## 1.2. Hugo is a CLI program
Hugo itself is an executable file. You interact with it via the command line (PowerShell, cmd, bash). 
 
See [Install Hugo Docs](https://gohugo.io/getting-started/installing/).

The two most important commands are `hugo`, and `hugo server`. 
If there's a valid Hugo project in the current directory, 
`hugo` will generate the site, and 
`hugo server` will host it on a local server so that you can see it in your browser. 

The `-h` flag displays help for any given command.

## 1.3. Hugo's separates content from layouts

In principle, you can write HTML/CSS/JS by hand to do a static site.
For many reasons this is inconvenient:

[^17]: Source: `<a href="https://example.com" rel="noopener noreferrer" target="_blank">example.com</a>`

* HTML is verbose compared to a plain document. For a link[^17] you will type 57 characters 
  plus the actual link. It's fine for one page, but it scales poorly.
* Typically some parts of the code are the same for all the pages, like styles, 
  fonts, links, etc. Even if you copy and paste everything it'll be tedious to do.
* If you want to make a change you'll have to do it on every file.
* Focus is divided between writing relatable content and handling the looks of the site. 
* Web design is its own field of knowledge and not everyone wants to invert time and effort on it. 

Hugo makes the process much easier by allowing you to separate static web design into two activities: content writing and template writing.

Content is written in [markdown](https://commonmark.org), which conceptually is a
syntactic sugar for HTML. Markdown is very easy to use. 

Templates are written in a HTML + a special templating language. Hugo generates the site by inserting the data from your content files into those templates. 

## 1.4. Society is divided into Theme Users and Theme Writers. 

If you just want to use a nice theme from the [Hugo Themes Page](https://themes.gohugo.io/),
you can start with the example site --every theme has one-- and use your intuition to add files
and configurations. No knowledge of the templates or even Web Design is required, all you need to do is 
to write all your content in markdown and browse [Content Management Docs](https://gohugo.io/content-management) 
and the theme documentation every once in a while.

But the day will come that you'll you need to tinker with the themes or write your own.

# 2. Info for Theme Users

## 2.1. Hugo projects have a definite directory structure

The top level of a Hugo project may have these: 

{{% dir %}}
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
{{%/ dir %}}

You can read about each of them at [Directory Structure Docs](https://gohugo.io/getting-started/directory-structure/). 
A config file is mandatory[^1], and the rest directories are optional and added as needed.[^15] 

[^15]: The folders can be configured to have dferent names, although this is not common.

[^1]: This isn't 100% true. The configs can be set at `/config` as pointed out in the
  [Configuration Directory Docs](https://gohugo.io/getting-started/configuration/#configuration-directory).

`/public` is created to store the generated files.
The files stand on their own: you can upload them to the static server and forget 
that you ever used Hugo to create them. 

## 2.2. Merge other Hugo projects to yours with Modules

[Hugo Modules](https://gohugo.io/hugo-modules/) offer a very flexible and understandable way of 
importing from other project. 

Suppose that you want to add the [`Ananke`](https://themes.gohugo.io/gohugo-theme-ananke/) 
theme to your site. You could clone the repository from `https://github.com/theNewDynamic/gohugo-theme-ananke` 
and copy and paste files into your project. 

But a cleaner method, more maintainable method is to: 

[^13]: If you **do** expect people to import your project then put the path that everyone
  will use to import your project. This is how it would look like: 
  `hugo mod init github.com/johndoe/my_module_project`. 
  See [Using Modules Docs](https://gohugo.io/hugo-modules/use-modules/) 

1. Run the command `hugo mod init path/to/your/project` which will initialize your project as a Hugo Module. If you don't 
  intend people to import your project, then `path/to/your/project` doesn't matter, you can put a `_`
  if you want.[^13]
2. Include the following lines in the config: 
    ```yaml 
    baseURL: https://example.com/ 
    # ... and everything else

    module:
      imports:
        - path: github.com/theNewDynamic/gohugo-theme-ananke
    ``` 

The result is almost the same as copy and pasting: the files from Ananke behave as 
if they were your own. Note that only these folders are merged: `archetypes`, 
`assets`, `content`, `data`, `i18n`, `layouts`, `static`. 

The advantages of doing this:
  * You can update the theme easily with the command 
    ```console
    hugo mod get -u github.com/theNewDynamic/gohugo-theme-ananke
    ```
  * When two files are in conflict (have the same path and name) your files are used. 
    You can always override a theme file with one of your own.
  * You can [mount specific directories](https://gohugo.io/hugo-modules/configuration/#module-config-mounts) instead of the whole project.
  
## 2.3. Content files are "front matter" + markdown

Any markdown `.md` file inside `/content` is called a **content file**[^8]. Each content file
is used to render a corresponding page. 

[^8]: Files other than markdown can be used, including html, pandoc, etc.
  [See the list of content formats](https://gohugo.io/content-management/formats/#list-of-content-formats)

Content files start with metadata variables defined in 
[YAML](https://yaml.org/), 
[JSON](https://www.json.org/), 
or [TOML](https://toml.io/en/). 
This part of the file is called **front matter**. Typical variables are title and date, among others. 
The rest of the file is in markdown.

Front matter variables have different effects on the generated page, some are Hugo-specific, 
and some are theme-specific. 
A big part of working with Hugo is figuring out which variables do what you want. 

The following three versions of `/content/hello-world.md` render the same page. Notice the different delimiters for each format:

* YAML Front Matter
  ```
  ---
  title: Hello World
  date: 2021-01-13T11:00:00-03:00
  ---
  ## Hello World!!
  In this article, I will...
  ```
* TOML Front Matter
  ```
  +++
  title = "Hello World"
  date = "2021-01-13T11:00:00-03:00"
  +++
  ## Hello World!!
  In this article, I will...
  ```
* JSON Front Matter
  ```
  {
    "title" : "Hello World",
    "date" : "2021-01-13T11:00:00-03:00"
  }
  ## Hello World!!
  In this article, I will...
  ```

## 2.4. Shortcodes extend markdown

Markdown falls short in some aspects. Some page elements like galleries or iframes can't
be conveniently represented. 

While the specification of markdown says that pure `HTML` is valid, Hugo skips it for safety
reasons. If you write `<h2> Hello </h2>` in a content file, you'll get
`<!-- raw HTML omitted -->` at the generated file. You can 
 [configure markup](https://gohugo.io/getting-started/configuration-markup#goldmark)
to make it "unsafe" and then add all the elements you need. 
But the advantage of markdown was to avoid writing plain HTML in the first place.

Another option is to use **shortcodes**: templates you can call from the content files 
to insert HTML into the page.  

Here's an example using the built-in `youtube` shortcode:

```none
---
title: Hello World
---
## Hello World!!
Before we start, see this video:

{‎{< youtube w7Ft2ymGmfc >}‎}
```

This produces the typical embedded code for Youtube videos: 

```html
<p>Before we start, see this video:</p>

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/w7Ft2ymGmfc" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="YouTube Video"></iframe>
</div>
```
There are different ways to use shortcodes:
* with named parameters
  ```none
  {‎{< youtube id="w7Ft2ymGmfc" autoplay="true" >}‎}
  ```
* raw string parameter
  ```none
  {‎{<  rawstringshortcode `This is some <b>HTML</b>,
  and a new line with a "quoted string".` >}‎}
  ```
* enclosing text, result is inserted into page directly
  ```none
  {‎{< highlight go >}‎} A bunch of code here {‎{< /highlight >}‎}
  ```
* enclosing text, result is inserted to content file, and then gets rendered as markdown.
  ```none
  {‎{% markdownshortcode %}‎}
  Stuff to `process` in the *center*. 
  {‎{% /markdownshortcode %}‎}
  ```
* self-closing (the following are equivalent)
  ```none
  {‎{<myshortcode>}‎}{‎{</myshortcode>}‎}
  {‎{< myshortcode />}‎}
  ``` 

Hugo comes with many built-in shortcodes and you can define your own by adding templates 
to `/layouts/shortcodes`. 

For reference on how to use and create shortcodes: 
* [Shortcodes - Content management](https://gohugo.io/content-management/shortcodes/) 
  for shortcode users. Includes complete list of built-in shortcodes.
* [Shortcodes - Templates](https://gohugo.io/templates/shortcode-templates/) for shortcode writers
* [Shortcode - Variables](https://gohugo.io/variables/shortcodes/) for shortcode writers as well. 

## 2.5. The generated site has the structure of `/content`

Suppose `/content` looks like this:

{{% dir %}}
* \d content 
  * \f _index.md
  * \d blog
    * \f _index.md
    * \f hello-world.md
    * \f see-you-later-world.md
  * \d presentations
    * \f _index.md
    * \f why-hugo.md
    * \f why-go.md
    * \d math
      * \f _index.md
      * \f quadratics.md
      * \f linear-algebra.md
{{%/ dir %}}

Then output has a similar structure:

{{% dir %}}
* \d public 
  * \f index.html
  * \d blog
    * \f index.html
    * \d hello-world
      * \f index.html
    * \d see-you-later-world
      * \f index.html
  * \d presentations
    * \f index.html
    * \d why-hugo
      * \f index.html
    * \d why-go.md
      * \f index.html
    * \d math
      * \f index.html
      * \d quadratics
        * \f index.html
      * \d linear-algebra
        * \f index.html
{{%/ dir %}}

And the final site will have these URLs once it's hosted:

* https://example.com/
* https://example.com/blog/
* https://example.com/blog/hello-world/
* https://example.com/blog/see-you-later-world/
* https://example.com/presentations/
* https://example.com/presentations/why-hugo/
* https://example.com/presentations/why-go/
* https://example.com/presentations/math/
* https://example.com/presentations/math/quadratics/
* https://example.com/presentations/math/linear-algebra/

There's a clear correspondence between `/content` structure, output files, and URL structure.[^7]

[^7]: This is a general rule. You can force the URLs to be different, which you can see in 
  [URL Management Docs](https://gohugo.io/content-management/urls/). 
  Also, the pages don't need to be contained in a single `.md`. 
  There's another way to organize content files called 
  [Page Bundles](https://gohugo.io/content-management/page-bundles/) 
  which allows you to divide each page on a separate directory where 
  you can also keep the images and resources specific to that page.

## 2.6. Pages are list pages or regular pages

Some important definitions: 

**List pages** are pages that contain **children** pages, and define the hierarchy of the site. 
The content file of a list page is its corresponding `_index.md`[^21].

[^21]: See [Lists of Content Docs](https://gohugo.io/templates/lists/).

**Sections**, a special case of list pages, are subdirs of `/content` that have an `_index.md`.[^2]
Its children are the pages under the section's directory, including other sections.

[^2]: As a special case, the first level children of `/content` are always sections. 
See [Sections Docs](https://gohugo.io/content-management/sections).

**Regular pages** are pages that can never have children.

In the previous example `blog`, `presentations` and `presentation/math` are sections.
The children of `presentations` are `presentations/why-hugo`,
`presentations/why-go`, and `presentations/math`. 

The regular pages are: 
* `hello-world`
* `see-you-later-world`
* `presentations/why-go`
* `presentations/why-hugo`
* `presentations/math/quadratics` 
* `presentations/math/linear-algebra`

# 3. Info for Theme Writers 

## 3.1. Templates are `HTML` with `{{...}}`

Hugo's template language is borrowed from [Go Templates](https://pkg.go.dev/text/template/). 
It has types, variables, functions, and statements (`if`, `with`, `range`, `define` and `block`). 

In this example a template renders a single page:

{{% dir %}}
* \f config.yaml
* \d content
  * \d blog
    * \f hello-world
      ```none
      ---
      title: Hello World
      ---
      ## Hello World!!
      In **this** article, I will...
      ```
* \d layouts
  * \d blog
    * \f single.html
      ```go-html-template
      <html>
      <head>
      <title> {{ upper .Title }} </title>
      </head>
      <body> 
      {{.Content}} 
      </body>
      </html>
      ``` 
      The `{{...}}` are placeholders.

      In the line 3, the [`upper`](https://gohugo.io/functions/upper) function receives the `.Title` variable as an argument.
      The value of `.Title` is set in the front matter of the content file. 

      Line 5 inserts the variable `.Content`. It contains the markdown converted to HTML, so `**this**` becomes `<strong>this</strong>` in the variable. 
* \d public
  * \d blog
    * \d hello-world
      * \f index.html      
        This is the final result:
        ```html
        <html>
        <head>
        <title> HELLO WORLD </title>
        </head>
        <body> 
        <h2 id="hello-world">Hello World!!</h2>
        <p>In <strong>this</strong> article, I will&hellip;</p>
        
        </body>
        </html>
        ```
{{%/ dir %}}

## 3.3. `/layouts` contains the HTML templates.
Each content file is rendered with a specific template from `/layouts` that is chosen 
using a [set of rules](https://gohugo.io/templates/lookup-order). 

A subset of rules I find convenient [^9] is:

* A regular page like `/content/my_type/**/foo.md` will be rendered using `/layouts/my_type/single.html`
* A section page like `/content/my_type/**/_index.md` will be rendered using `/layouts/my_type/list.html`.  
* `/layouts/_default/single.html` and `/layouts/_default/list.html` are used if the others are missing.

[^9]: There are many other ways to organize templates, see [Template Lookup Order](https://gohugo.io/templates/lookup-order). It's a matter of preference. 

## 3.4. The dot has the current context

The dot stores the variables that can be accessed at a given point in the program. 
That's why in the previous example `.Content` and `.Title` begin with a dot. 

The dot changes meaning inside `range` and `with` blocks. 
The variables available inside and outside of those blocks are different.

## 3.5. Variables depend on front matter, config, or position. 

`.Title` is an example of Hugo-specific front matter-defined variables. 

Some variables can be accessed from any template (_global_ variables). 
For example, if at `config.yaml` you define `author: John Doe`, you can use that variable
in the templates as `.Site.Author`. 

Other variables are related to the position of the file in `/content`.

For example, list pages have a `.Pages` variable that is a slice[^4] of page variables 
of the children of the page.

[^4]: slices are known as "array" in other languages

See the complete lists of variables at
[Site Variables](https://gohugo.io/variables/site) and
[Page Variables](https://gohugo.io/variables/page)

## 3.6. `range` and `.Pages` are useful to list links

In the following example, suppose that you want the section page of the blog 
at `https://example.com/blog` to list all the links to the posts so that the users 
can visit them.

To do this use: 
  * `.Pages`, and `.Title` discussed previously
  * the `range` block, which iterates over slices and dicts[^5].
  * `.Permalink`, a page variable that contains the full URL to the page.

[^5]: also known as `maps`

Here's the full example:

{{% dir %}}
* \f config.yaml
  ```yaml
  baseURL: https://example.com/
  ``` 
* \d content 
  * \f _index.md
  * \d blog 
    * \f _index.md 
      ```none
      ---
      title: Blog
      ---
      Welcome to the blog! See the posts:
      ``` 
    * \f hello-world.md
      ```none
      ---
      title: Hello World!
      ---
      In this article, I will...
      ``` 
    * \f see-you-later-world.md
      ```none
      ---
      title: See you later World!
      ---
      In this article, I will...
      ``` 
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
      {{.Content}}
      <ol>
      {{ range .Pages }}
        <li>
        <a href="{{ .Permalink }}">{{ .Title }}</a>
        </li>
      {{ end }}
      </ol>
      </body>
      </html>
      ```
      Inside the range block, the dot means "the current iteration". 

      As a result, `.Title` doesn't mean "the title of the current page", but 
      instead means "the title of the _current iteration_ page". 
      This is called **rebinding** the context.[^10]

      [^10]: When the context has been rebinded, you lose access to the original Page variables.
        Conveniently, the variable `$` is set to the initial value of the dot. 
        You use it from inside the block as `{{$.Title}}` to get the variables back.
        See [Use $ to access the global context](https://gohugo.io/templates/introduction/#2-use--to-access-the-global-context)

* \d public
  * \d blog 
    * \f index.html
      ```html
      <html>
      <head>
      <title> Blog </title>
      </head>
      <body>
      <p>Welcome to the blog! See the posts:</p>

      <ol>

        <li>
        <a href="https://example.com/blog/hello-world/">Hello World!</a>
        </li>

        <li>
        <a href="https://example.com/blog/see-you-later-world/">See you later World!</a>
        </li>

      </ol>
      </body>
      </html>
      ```
{{%/ dir %}}

## 3.7. `.Params` stores the Non-Hugo-specific variables

Some variables on the config or the front matter that **don't** have a special meaning to Hugo.
You can access those variables through either the `.Params` or `.Site.Params` dictionaries. 

### 3.7.1 How to use Variables defined on the Front matter of a page

{{% dir %}}
* \f config.yaml
* \d content
  * \d blog
    * \f hello-world.md
      ```
      ---
      title: Hello
      my_custom_variable: im a custom variable
      ---
      In this article, I will...
      ``` 
* \d layouts
  * \d blog
    * \f single.html
      ```go-html-template
      <html>
      <body>
        <p> The value is: {{.Params.my_custom_variable}} </p>
      </body>
      ```
* \d public
  * \d blog
    * \d hello-world
      * \f index.html
        ```html
          <html>
          <body>
            <p> The value is: i'm a custom variable </p>
          </body>
          </html>
        ``` 
{{%/ dir %}}

### 3.7.2 How to use Site Variables defined in the config

For site variables defined in the config, you have to define them inside the `params` object 
on the config, and they are stored in `.Site.Params`.

{{% dir %}}
* \f config.yaml
  ```yaml
  baseURL: https://example.com
  params: 
    my_custom_variable: im a custom variable
  ```
* \d content
  * \d blog
    * \f hello-world.md
* \d layouts
  * \d blog
    * \f single.html
      ```go-html-template
      <html>
      <body>
        <p> The value is: {{.Site.Params.my_custom_variable}} </p>
      </body>
      </html>
      ```
* \d public
  * \d blog
    * \d hello-world
      * \f index.html
        ```html
        <html>
        <body>
          <p> The value is: i'm a custom variable </p>
        </body>
        </html>
        ``` 
{{%/ dir %}}

## 3.8. Template variables are declared with `‎ := ‎` and updated with `‎ = ‎`

For convenience during template writing, you can declare internal variables with:

```go-template-html
{{ $a := "hello" }}
{{ $a = "HELLO" }}
{{ $a }}
```

In the first line, `$a` is declared and set to `"hello"`. Then, it changes its value to "HELLO". Finally, it's printed on the template. 

It's an error to use `=` to a variable that hasn't been declared with `:=` before: [^18]

```go-template-html
{{ $b }}
```
```console {wrap}
$ hugo
Error: 
add site dependencies: 
load resources: 
loading templates: "C:\Users\agust\concepts-of-hugo\3.8-template-variables\layouts\blog\single.html:12:1":
parse failed: 
template: 
blog/single.html:12: 
undefined variable "$b"
```

[^18]: Another common error is to accidentally define a variable twice in different contexts: 
    ```go-template-html
    {{ $a := 0 }}
    {{ range (slice 1 2 3) }}
      {{ $a := . }}
      {{ $a }}
    {{ end }}
    {{ a }}
    ```
    The result here is "1 2 3 0", instead of "1 2 3 3". `$a` is declared in the initial
    context, and then a _different_ `$a` gets declared inside the range block. This can lead
    to unexpected results.
    
    To get the "1 2 3 3" version, put `$a = . ` at the fourth line. 

## 3.9. Handle missing values with `if`, `with`, and `default`

The previous example is a bit fragile, because the templates are called using many 
different content files. If `my_custom_variable` doesn't exist in one of them, 
the whole build fails.

Here are three methods to avoid that: 

[^11]:  See [`isset` Docs]((https://gohugo.io/functions/isset)).

### 3.9.1 if
```go-template-html
{{ if (isset .Params "my_custom_variable") }}
    <p> The value is: {{ .Params.my_custom_variable }} </p>
{{ else }} 
  <p> my_custom_param not set </p>
{{ end }}
```
This example is just to show how the `if` statement works. The `{{else}}` block is optional. 
The `isset` function[^11] returns `true` if the 
second argument is set in the first argument, and `false` otherwise. 
  
### 3.9.2 with
```go-template-html
{{ with .Params.my_custom_param }}
<p> The value is: {{.}} </p>
{{ end }}
```
The block is run if `.Params.my_custom_param` is set, and **not** run if it's
missing. `with` rebinds the context: inside the block, the dot means "the variable of the `with`", in this case `my_custom_param`.

### 3.9.3 default
```go-template-html
{{ $a := default "my_default" .Params.my_custom_variable }}
{{ $a }}
```
The [default](https://gohugo.io/functions/default/) function outputs a default 
value if a variable is not set.
In this case, if `.Params.my_custom_variable` is not set, so `$a` it takes the value of `"my_default"`.
  

## 3.10. Parenthesis clarify how the functions are applied 

Like in math, parenthesis are used to disambiguate the order of application in
 a long sequence of functions:

```go-template-html
{{ markdownify (upper (emojify "## hello :‎smiley:")) }}
```

1. `emojify` is applied to `"## hello :‎smiley:"` which results in `"## hello 😀"`
2. `upper` is applied to `"## hello 😀"` which results in `"## HELLO 😀"`
3. `markdownify` is applied to `"## HELLO 😀"`, which turns it into `"<h2> HELLO 😀</h2>"`

## 3.11. Pipe operator = less parenthesis

The pipe operator `‎ | ‎` is a syntactic sugar that passes the output from the left of the operator to 
the function to the right, as the last argument. 

This is equivalent to the previous example: 

```go-template-html
{{ "## hello :‎smiley‎:" | emojify | upper | markdownify }}
```
The output is exactly the same as before. Notice that there are less parenthesis used. 

## 3.12. Partials keep templates DRY

Certain elements of a site appear on multiple templates, such as menus or footers.
It would be inconvenient to rewrite the same patterns across all templates. 

**Partials** allow you to reuse code. A partial is a template stored in `/layouts/partials` 
that can be called from other templates. 

In the following example, a footer is separated into its own partial so that it can be 
used in many templates:

{{% dir %}}
* \f config.yaml
  ```yaml
  baseURL: https://example.com/
  ```
* \d content
  * \d blog
    * \f hello-world.md
      ```none
        ---
        title: Hello
        ---
        ## Hello World!
        In this article, I will...
      ``` 
* \d layouts
  * \d partials
  * \d blog
    * \f single.html
      ```go-template-html
      <html>
      <head> 
        <title> {{.Title}} </title>
      </head>
      <body> 
        {{.Content}}
      </body>
      {{ partial "my_footer.html" . }}
      </html>
      ```
      The first argument is the path to the template relative to `/layouts/partials`, and the second
      argument is the context passed. In other words, inside the partial template Hugo will use the 
      second argument as the dot.

    * \f my_footer.html
      ```go-template-html
      <footer> 
      Site made with :heart: and Hugo.  
      <a href="{{.Site.Home.Permalink}}"> Return to Homepage</a>
      </footer>
      ```
* \d public 
  * \d blog
    * \d hello-world
      * \f index.html
        ```html
        <html>
        <head> 
          <title> Hello </title>
        </head>
        <body> 
          <h2 id="hello-world">Hello World!</h2>
        <p>In this article, I will&hellip;</p>

        </body>
        <footer> 
        Site made with ❤️ and Hugo.  
        <a href="https://example.com/"> Return to Homepage</a>
        </footer>
        </html>
        ```
{{%/ dir %}}

# Footnotes