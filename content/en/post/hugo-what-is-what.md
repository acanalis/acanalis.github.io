---
title: Hugo What is What
subtitle: Fundamentals of Hugo
date: 2021-01-13T11:00:00-03:00
_build:
  list: never

url: /drafts/fast-hugo-intro
summary: Learn [Hugo](https://gohugo.io) efficiently! Before you go on a quest to read the whole documentation
  Read these 25 key points.
---

Starting with [Hugo](https://gohugo.io) _The world’s fastest framework for building websites_, 
it's difficult to make sense of all the new vocabulary and concepts. 
The usual way to learn is to install Hugo, try out the 
[Quick start](https://gohugo.io/getting-started/quick-start/), and then navigate enough
documentation pages until everything makes sense.

The Hugo Docs, while very precise, don't provide a learning order. Tutorials 
usually are written to achieve a certain goal (_how to do X with Hugo_) but don't go into 
depth on how Hugo works. 

This article is an attempt to give beginners a "what is what" introduction to Hugo that seems to 
be missing. The objective is to explain 90% of how Hugo works in 25 key points, with the hope of
making the rest of the learning experience easier.

This article is for beginners to Hugo. This is not the place to mention exceptions and special
 rules; if necessary, I'll put them in footnotes.
Visit [Hugo Docs](https://gohugo.io/documentation) for the most precise and up-to-date explanations.

{{< toc >}}

# Info for Everyone

## Hugo is a static site generator
A static site is one which can be served from a static server. A static server's only 
job is to provide the necessary files `*.html, *.js, *.css, etc`  to the clients.

Every client gets the same files: there's no server-side intelligence or interaction.
Interaction is possible, but using JavaScript on the client-side.

## Hugo is a CLI program
Hugo itself is an executable file. You interact with it via the command line (PowerShell, cmd, bash). 
 
After you [install Hugo](https://gohugo.io/getting-started/installing/)
you can run `hugo`, or `hugo server`, the two most important commands. If there's a 
valid Hugo project in the current directory, `hugo` will generate the site, and `hugo server`
will host it on a local server so that you can see it in your browser. 

The `-h` flag displays help for any given command.

Some familiarity with command line interface programs is needed. 

## Hugo's separates content from layouts

In principle, you can write HTML/CSS/JS by hand to do a static site.
For many reasons this is inconvenient:

[^17]: Slight exaggeration of: `<a href="https://example.com" rel="noopener noreferrer" target="_blank">example.com</a>`

* HTML is verbose compared to a plain document. For a link[^17] you will type 57 characters 
  plus the actual link. It's fine for one page, but it scales poorly.
* Typically some parts of the code are the same for all the pages, like certain analytics, 
  fonts, links, etc. Even if you copy and paste everything it'll be tedious to do
* If you want to make a change you'll have to do it manually on every file.
* Focus is divided between writing relatable content and handling the looks of the site. 
* Web design is its own field of knowledge and not everyone wants to invert time and effort 
  on that. 

Hugo makes This is the problem that Hugo aims to solve by allowing you to separate web design into 
two activities: content writing and template writing.

Content is written in [markdown](https://commonmark.org), which conceptually is a condensed
syntactic sugar for HTML. Markdown is very easy to use. 

Templates are written in a special templating language, and Hugo will use them 
to turn your content files into the HTML your static site needs. 

## Society is divided into Theme Users and Theme Writers. 

If you just want to use a nice theme from the [Hugo Themes Page](https://themes.gohugo.io/),
you can start with the example site --every theme has one-- and then use your intuition to add files
and configurations. No knowledge of the templates or even Web Design is required, all you need is 
to write all your content in markdown and browse [Content Management Docs](https://gohugo.io/content-management) 
and the theme documentation every once in a while.

But the day will come that you'll you need to tinker with the themes or write your own.

# Info for Theme Users

## Hugo projects have a definite directory structure

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

You can read about each of them at [Directory Structure Docs](https://gohugo.io/getting-started/directory-structure/). 
A config file is mandatory[^1], and the rest directories are optional and added as needed.[^15] 

[^15]: The folders can be configured to have different names, although this is not common.

[^1]: This isn't 100% true. The configs can be set at `/config` as pointed out in the
  [Configuration Directory Documentation](https://gohugo.io/getting-started/configuration/#configuration-directory).

`/public` is created to store the generated files.
The files stands on their own: you can upload them to the static server and forget 
that you ever used Hugo to create them. 

## Merge other Hugo projects to yours with Modules

[Hugo Modules](https://gohugo.io/hugo-modules/) offer a very flexible and understandable way of 
importing from other project. 

Suppose that you want to add the [`Ananke`](https://themes.gohugo.io/gohugo-theme-ananke/) 
theme to your site. You could clone the repository from `https://github.com/theNewDynamic/gohugo-theme-ananke` 
and copy and paste files from that project into yours. 

But the cleaner method, more maintainable method is to: 

[^13]: If you **do** expect people to import your project then put the path that everyone
  will use to import your project. This is how it would look like: 
  `hugo mod init github.com/johndoe/my_module_project`. 
  See [Documentation on Using Modules](https://gohugo.io/hugo-modules/use-modules/) 

* Run the command `hugo mod init path/to/your/project` which will initialize your project as a Hugo Module. If you don't 
  intend people to import your project, then `path/to/your/project` doesn't matter, you can put a `_`
  if you want.[^13]
* Include the following lines in the config: 
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
  * You can update easily with the command 
    ```console
    hugo mod get -u github.com/theNewDynamic/gohugo-theme-ananke
    ```
  * When two files are in conflict (have the same path and name) your files are used. 
    You can always override a theme file with one of your own.
  * You can [mount specific directories](https://gohugo.io/hugo-modules/configuration/#module-config-mounts) instead of the whole project.[^14]
  
## Content files are "front matter" + markdown

Any markdown `.md` file inside `/content` is called a **content file**[^8]. 
A corresponding page will rendered with the information contained in it. 

[^8]: Files other than markdown can be used, including html, pandoc, etc.
  [See the list of content formats](https://gohugo.io/content-management/formats/#list-of-content-formats)

Content files start with metadata variables defined in YAML, JSON, or TOML. This part of the file
is called **front matter**. Typical variables are title and date, among others. 
The rest of the file is in markdown.

Front matter variables have different effects on the generated page, some are Hugo-specific, 
and some are theme-specific. 
A big part of working with Hugo is figuring out which variables do what you want. 

The following three versions of `/content/hello-world.md` have the same effect. Notice the different delimiters for each format:

* YAML Front Matter
  ```
  ---
  title: Hello
  date: 2021-01-13T11:00:00-03:00
  ---
  ## Hello World!
  In this article, I will...
  ```
* TOML Front Matter
  ```
  +++
  title = "Hello"
  date = "2021-01-13T11:00:00-03:00"
  +++
  ## Hello World!
  In this article, I will...
  ```
* JSON Front Matter
  ```
  {
    title : "Hello",
    date : "2021-01-13T11:00:00-03:00"
  }
  ## Hello World!
  In this article, I will...
  ```

## Shortcodes extend markdown

Markdown falls short in some aspects. Some page elements like galleries or iframes can't
be conveniently represented. 

While the specification of markdown says that pure `HTML` is valid, Hugo skips it for safety
reasons. If you write `<h2> Hello </h2>` in a content file, you'll get
`<!-- raw HTML omitted -->` at the generated file. You can 
 [configure markup](https://gohugo.io/getting-started/configuration-markup#goldmark)
to make it "unsafe" and then add all the elements you need. 

But this isn't ideal because the we were writing markdown was to avoid plain HTML in the first place. 

A friendlier option is to use **shortcodes**: functions you can call from the content files 
that insert HTML into the page.  

Here's an example using the built-in `youtube` shortcode:

```yaml
---
title: Hello
date: 2021-01-13T11:00:00-03:00
---
## Hello World!

Before we start, see this video:

{‎{< youtube w7Ft2ymGmfc >}‎}

```

Upon finding that shortcode call Hugo runs the template and produces the typical 
embedded code for Youtube videos: 

```html
<p>Before we start, see this video:</p>

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/w7Ft2ymGmfc" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="YouTube Video"></iframe>
</div>
```
Some shortcodes are called differently:
* with named parameters
  ```none
  {‎{< youtube id="w7Ft2ymGmfc" autoplay="true" >}‎}
  ```
* raw string parameter
  ```none
  {‎{<  myshortcode `This is some <b>HTML</b>,
  and a new line with a "quoted string".` >}‎}
  ```
* enclosing text, result is inserted into page directly
  ```none
  {‎{< highlight go >}‎} A bunch of code here {‎{< /highlight >}‎}
  ```
* enclosing text, result is inserted to content file, and then gets rendered as markdown.
  ```none
  {‎{% mdshortcode %}‎} Stuff to `process` in the *center*. {‎{% /mdshortcode %}‎}
  ```
* self-closing (the following are equivalent)
  ```none
  {‎{< highlight >}‎}{‎{</ highlight >}‎}
  {‎{< highlight />}‎}
  ``` 

The documentation of each shortcode will specify which are the appropriate ways of calling it. 

Hugo comes with many built-in shortcodes and you can define your own by adding templates 
to `/layouts/shortcodes`. 

For reference: 
* [Shortcodes - Content management](https://gohugo.io/content-management/shortcodes/) 
  for shortcode users. Includes complete list of built-in shortcodes.
* [Shortcodes - Templates](https://gohugo.io/templates/shortcode-templates/) for shortcode writers
* [Shortcode - Variables](https://gohugo.io/variables/shortcodes/) for shortcode writers as well. 

## The generated site has the structure of `/content`

Suppose `/content` looks like this:

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

Then output has a similar structure:

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

And the final site will have these URLs available once it's hosted:

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
There's a clear correspondence between `/content` structure, output site, and URL structure.[^7]

[^7]: This is a general rule. You can force the URLs to be different, which you can see in 
  [the documentation of URL Management](https://gohugo.io/content-management/urls/). 
  Also, the pages don't need to be contained in a single `.md`. 
  There's another way to organize content files called 
  [Page Bundles](https://gohugo.io/content-management/page-bundles/) 
  which allows you to divide each page on a separate directory where 
  you can also keep the images and resources specific to that page.

# Info for Theme Writers 

## Sections are subdirs of `/content` that have an `_index.md` [^2]

[^2]: As a special case, the first level children of `/content` are always sections. See the [Docs for Sections](https://gohugo.io/content-management/sections). 
  Also, in this section I'm omitting that taxonomy lists and terms have a corresponding `_index.md`, 
  but those are not considered sections. 

In the previous example `/`, `/blog`, `/presentations` and `/presentation/math` were sections.

All the pages under a section's directory (including other sections) are called its children. 
The children of `presentations` are, for example, `why-hugo`, `why-go` and `math`. 
This definition will become important later on.

Non-section pages are simply called a **regular pages**.

## `/layouts` contains the HTML templates.
Each content file is matched with a specific template from `layouts`, with a [set of rules](https://gohugo.io/templates/lookup-order). 

This is a subset of rules I find convenient [^9]:

* A regular page like `content/somepath/**/foo.md` will be rendered using `layouts/somepath/single.html`
* A section page like `content/somepath/**/_index.md` will be rendered using `layouts/somepath/list.html`.  
* `layouts/_default/single.html` and `layouts/_default/list.html` are used if the others are missing.

[^9]: There are many other ways to organize templates, see [Template Lookup Order](https://gohugo.io/templates/lookup-order). It's a matter of preference. 

## Templates are `HTML` sprinkled with `{{...}}`

Hugo's template language is borrowed from [Go Templates](https://pkg.go.dev/text/template/). 
It has types, variables, functions, and `if`-`range`-`with` statements. 

Consider the following `content/blog/hello-world.md` file:

```none
---
title: Hello
---
## Hello World
```

This will be rendered using `layouts/blog/single.html`:

```go-html-template
<html>
<head>
<title> {{ upper .Title }} </title>
</head>
<body> 
{{.Content}} 
</body>
```

Hugo will are replace all the `{{...}}` with different values.

In the first one, the [`upper`](https://gohugo.io/functions/upper) function receives the `.Title` variable as an argument.
The value of `.Title` is set in the front matter of the content file. 

In the second clause, the variable `.Content` is inserted. 
It contains the content itself of the content file, but with the markdown already rendered to HTML.
This means that, for example, `## Hello` turns into `<h2> Hello </h2>`. 

The generated file would look like this: 

```html
<html>
<head>
<title> HELLO </title>
</head>
<body> 
<h2> Hello World </h2>
</body>
```

## The dot contains the available variables

The dot stores "the current context", in other words all the variables that 
can be accessed from a given point in the program. That's why in the previous example
`.Content` and `.Title` begin with a dot. 

Note that the context --and thus the dot-- a might change along the code.

## Hugo-specific variables depend on front matter, config, or position. 

`.Title` is an example of Hugo-specific front matter-defined variables. 

Some variables defined in the config can be accessed from any template (_global_ variables). `.Site.Author`, for example, can be defined in `config.yaml` as `author: John Doe`.

Some variables, such as `.Pages`, are related to the position of the file 
in `/content`. It's available in section pages[^3]; it's a slice[^4] of the page variables of all the children 
of the section. 

[^3]: `.Pages` is also available in taxonomy terms, taxonomy list, homepage and RSS pages. 
  See [documentation on lists of content](https://gohugo.io/templates/lists/)
[^4]: slices are known as "array" in other languages

For reference: [List of Site Variables](https://gohugo.io/variables/site), [List of Page Variables](https://gohugo.io/variables/page)

## List all the pages in a section with `range` and `.Pages`

The `range` block is used to iterate over slices and dicts[^5].

[^5]: also known as `maps`

As an example, let's say that your website has a blog section at `www.example.com/blog`,
and you want to list links to the posts so that the user can visit them.

This is what your project looks like, including the template: 
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

Inside the range block, the dot means "the current iteration". 
As a result, `.Title` doesn't mean "the title of the current page" as usual, but 
instead means "the title of the **current iteration** page". 
This is called **rebinding** the context.[^10]

[^10]: When the context has been rebinded, you lose access to all the Page variables.
  In case you need them within the range, use the variable `$`. It's set to the initial value of 
  the dot. Here's how it looks: `{{$.Site.Title}}`. See [Use $ to access the global context](https://gohugo.io/templates/introduction/#2-use--to-access-the-global-context)

This is the result at `/public/blog/index.html`:

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

## Access Non-Hugo-specific variables with `.Params`

When you write a variable on the config or the front matter that **doesn't** have a special meaning to Hugo, you have access to it through the `.Params` dictionary. 

Here's an example for a front matter defined variable:

```
---
title: Hello
my_custom_variable: "im a custom variable"
---
```
So to use it in the template: 

```go-html-template
<p> The value is: {{.Params.my_custom_variable}} </p>
```

For variables defined in the config, there's a slight difference: your variables have to be defined as **as elements of `params`**:

```yaml
baseURL: https://example.com
params: 
  my_custom_variable: "im a custom variable"
```
Then in any template:
```go-html-template
<p> The value is: {{.Site.Params.my_custom_variable}} </p>
```

## Declare a template variable with `‎ := ‎`, change its value with `‎ = ‎`

For convenience during template writing, you can declare internal variables with:

```go-template-html
{{ $a := "hello" }}
{{ $a = "HELLO" }}
{{ $a }}
```

In the first line, `$a` is declared and set to `"hello"`. Then, it changes its value to "HELLO". Finally, it's printed on the template. 

## Two pitfalls with template variables

It's an error to use `=` to a variable that hasn't been declared with `:=` before. 

Another common error is to accidentally define a variable twice in different contexts: 

```go-template-html
{{ $a := 0 }}
{{ range (slice 1 2 3) }}
  {{ $a := . }}
  {{ $a }}
{{ end }}
{{ a }}
```
The result here is 0, instead of the expected 3. The reason is that `$a` is declared in the initial
 context, and then another, _different_ `$a` gets declared in the context of the range.
The third line should be changed to `$a = .`

It's difficult to understand when you start with Hugo, the difference is subtle and
 it's very difficult to search in the documentation. I just hope that you never run into this.

## Handle missing values with `if`, `with`, and `default`

The previous example is a bit fragile, because the templates are called using many different content files. If `my_custom_variable` doesn't exist in one of them, the whole build fails.

Here are three methods to avoid that: 

[^10]:  See [the documentation for `isset`]((https://gohugo.io/functions/isset)) if you want.

* `if`: This example is just to show how the `if` statement works. 
  For this it's sufficient to know that the `isset` function[^10] returns `true` or `false`. 
  ```go-template-html
  {{ if (isset .Params "my_custom_variable") }}
     <p> The value is: {{ .Param.my_custom_variable }} </p>
  {{ end }}
  ```
* `with`: The block is run if `.Params.my_custom_param` is set, and **not** run if it's
  missing. `with` rebinds the context: inside the block, the dot means "the variable next to `with`", in this case `my_custom_param`.
  ```go-template-html
  {{ with .Params.my_custom_param }}
    <p> The value is: {{.}} </p>
  {{ end }}
  ```
* [`default`](https://gohugo.io/functions/default/) : This is a very common function to set defaults. 
  If `.Param.my_custom_variable` doesn't exist, it takes the value of `"a default value just in case"`
  ```go-template-html
  {{ $variable := default "a default value just in case" .Param.my_custom_variable }}
  {{ $variable }}
  ```

## Parenthesis clarify how the functions are applied 

If a long sequence of functions need to be applied, parenthesis are used to disambiguate 
the order of application

```go-template-html
{{ markdownify (upper (emojify "## hello :‎smiley:")) }}
```

In this case: 
1. `emojify` is applied to `"## hello :‎smiley:"` which results in `"## hello 😀"`
2. `upper` is applied to `"## hello 😀"` which results in `"## HELLO 😀"`
3. `markdownify` is applied to `"## HELLO 😀"`, which turns it into `"<h2> HELLO 😀</h2>"`

## Use the pipe operator `|` to save some parenthesis.

The pipe operator `|` is a syntactic sugar that passes the output from the left of the operator to 
the function to the right of the operator the **last argument**. 

The previous example would be written as: 

``` go-template-html
{{ "## hello :smiley:" | emojify | upper | markdownify }}
```

The output is exactly the same. Notice that there are less parenthesis used. 

## Partials are like custom functions for templates




