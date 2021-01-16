---
title: "Hugo: What is What"
date: 2021-01-13T11:00:00-03:00
_build:
  list: never

url: /drafts/fast-hugo-intro
summary: Learn [Hugo](https://gohugo.io) efficiently! Before you go on a quest to read the whole documentation
  Read these 20 key points.
---

Starting with [Hugo](https://gohugo.io) _The world’s fastest framework for building websites_ , it's a bit difficult to make sense of all the new
vocabulary and concepts. Usual way to learn is to install Hugo, try out the 
[Quick start](https://gohugo.io/getting-started/quick-start/), and then navigate the 
documentation until everything makes sense. That is difficult because there's no general summary
 of Hugo concepts in the docs. You need to visit the page of each topic 
 in order to see the wider picture.

This article is an attempt to condense all the essential information in 20 key points. 
The objective is to explain 90% of how Hugo works and to make the rest of the learning easier.

This article is for people with some background on Web design (HTML/CSS/JS) but beginners to Hugo.
Some exceptions and special rules are omitted for the sake of clarity, but I'll put them in footnotes.
Visit [Hugo Docs](https://gohugo.io/documentation) for the most precise and up-to-date explanations.

{{< toc >}}

## Hugo is a static site generator
A static site is one which can be served from a static server. A static server's only 
job is to provide the necessary `*.html, *.js, *.css, etc` files to the clients.

Every client gets the same files: there's no server-side intelligence or interaction.
Interaction is possible, but using JavaScript on the client-side.

## Hugo is a CLI program
Hugo itself is an executable file with which you interact via the 
command line (PowerShell, cmd, bash). 

With Hugo installed, and with a Hugo project in the current directory, 
you can run `hugo`, which generates the site, or `hugo server`, which 
hosts the site in a local server so that you can see it in your browser. These are the two most important commands. 

The `-h` flag displays help for any given command.

Some familiarity with command line interface programs is needed. 

## Hugo's value is in separating content from layouts

In principle, you can write HTML/CSS/JS by hand to do a static site. This is inconvenient:

* HTML is tedious to write. For a simple link you will type an extra 57 characters: `<a href="example.com" rel="noopener noreferrer" target="_blank">example.com</a>`.
  It's fine for one page, but it scales poorly.
* Typically some parts of the code are the same for all the pages, like certain analytics, fonts, links, etc.
* Even if you copy and paste everything it'll be tedious to do, and more importantly, I'll be impossible to make changes in an elegant way.
* You are focusing on two problems at once. Maybe you want to write the Best Cookie Recipe in the world,
  but now you are in a sidequest trying to figure out which CSS property centers your image. It's unproductive. 
* You have to actually know what you are doing. If frontend programming is outside your area of 
  expertise, it will take a lot of learning to make a production-grade website. That's not a top priority 
  for everyone. 

Hugo allows you to treat content and layout into two distinct activities. 

Content is written in [markdown](https://commonmark.org), which conceptually is a condensed
syntactic sugar for HTML. Markdown is very simple to understand and use. 

Hugo will turn those files into HTML by the rendering markdown 
and inserting it into the layout templates written in a special templating language. 

## Society is divided into Theme users and Theme writers. 

If you just want to use a nice theme you saw at the [Hugo Themes Page](https://themes.gohugo.io/),
you can start with the example site (every theme has one) and then use your intuition to add files
and configurations. No knowledge of the templates or even Web Design is required, you'll just 
write all your content in markdown, and browse the [Content Management](https://gohugo.io/content-management) part of the Docs and
the documentation of the chosen theme every once in a while.

But if you need to tinker with the themes or you want to write your own, 
you will need to know about the underlying system. 

## Hugo projects have a definite directory structure. 
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

Each one has a specific use. The config file (`/config.yaml,toml,json`) is mandatory[^1], 
and the rest directories are optional and added as needed. 

[^1]: This isn't 100% true. The configs can be set at `/config` as pointed out in the
  [Configuration Directory Documentation](https://gohugo.io/getting-started/configuration/#configuration-directory).

`/public` is the default[^6] output directory: it is created to store the generated files.
It stands on its own: you can upload just those files to the static server and forget that you ever used Hugo to create them. 

[^6]: the output directory can be changed using the `publishDir` configuration variable: in `config.yaml`: `publishDir: docs`.

## Content files are "front matter" + markdown.

Any markdown `.md`[^8] file inside `/content` is called a **content file**. 
A corresponding page will rendered with the information contained in it. 

[^8] Files other than markdown can be used, including html, pandoc, etc.
  [See the list of content formats](https://gohugo.io/content-management/formats/#list-of-content-formats)

Content files start with a **front matter**, a section written YAML, JSON, or TOML that defines 
metadata variables of the page. Typically title and date are defined, among others. 
Markdown is used for the rest of the file.

Front matter variables have different effects on the generated page. 
Some are Hugo-specific, and some are Theme-specific. 
A big part of working with Hugo is figuring out which variables to set to do what you want. 

The following three versions of `/content/hello-world.md` have the same effect. Notice the different delimiters for each format:

* YAML Front Matter
  ```
  ---
  title: Hello
  date: 2021-01-13T11:00:00-03:00
  ---
  ## Hello World!
  ```
* TOML Front Matter
  ```
  +++
  title = "Hello"
  date = "2021-01-13T11:00:00-03:00"
  +++
  ## Hello World!
  ```
* JSON Front Matter
  ```
  {
    title : "Hello",
    date : "2021-01-13T11:00:00-03:00"
  }
  ## Hello World!
  ```

## The generated site mirrors the structure of `/content`

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

The output has the same shape:

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

And the final site will look like this once it's hosted:

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

## Any subdir of `/content` that has an "_index.md" is a **section**[^2]

[^2]: In reality, the first level children of `/content` are always sections, regardless of whether
  they have `_index.md` or not. See the [Docs for Sections](https://gohugo.io/content-management/sections). 
  Also, in this section I'm also omitting that taxonomies can have a corresponding `_index.md`, 
  but those are not considered sections. In the end, the logic is almost the same.

Thus in the previous example, `/`, `/blog`, `/presentations` and `/presentation/math`
are **sections**. 

All the pages under a section's directory are called its children. 
The children of `presentations` are, for example, `why-hugo`, `why-go` and `math`. 
This definition will become important later on.

Anything else is simply called a **regular page**.

## `/layouts` contains the HTML templates.
Each page is rendered by inserting the variables and text from the content file into certain positions an HTML template. 
Out of the many templates located in `/layouts`, a specific one is selected for each page using a [wide set of rules](https://gohugo.io/templates/lookup-order). 

This is subset of rules I find convenient [^9]:

* A regular page like `content/somepath/**/foo.md` will be rendered using `layouts/somepath/single.html`
* A section page like `content/somepath/**/_index.md` will be rendered using `layouts/somepath/list.html`.  
* `layouts/_default/single.html` and `layouts/_default/list.html` are used if the others are missing.

[^9]: Many other structures are possible, it's a matter of preference. 
  The one I chose to is the easiest to learn.

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

The dot might change meaning along the code, if _"the context is rebinded"_. More on this later.

## Hugo-specific variables depend on front matter, config, or position. 

`.Title` is an example of Hugo-specific front matter-defined variables. 

Some variables defined in the config can be accessed from any template (_global_ variables). `.Site.Author`, for example, can be defined in `config.yaml` as `author: John Doe`.

Some variables, such as `.Pages`, are related to the position of the file 
in `/content`. 
`.Pages` is available in section pages[^3]; it's a slice[^4] of page variables of all the children 
of the section. 

[^3]: And in taxonomy terms, taxonomy list, homepage and RSS pages. 
  See [documentation on lists of content](https://gohugo.io/templates/lists/)
[^4]: also known as "array" on other languages

For reference: [List of Site Variables](https://gohugo.io/variables/site), [List of Page Variables](https://gohugo.io/variables/page)

## List all the pages in a section with `range` and `.Pages`

The `range` block is used to iterate over slices and dicts[^5].

[5]: also known as `maps`

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
This is called _rebinding_ the context.[^10]

[^10]: 2.  When the context has been rebinded, you lose access to all the Page variables and so on.
  In case you need them, then use the `$`. It's a variable that is set to the initial value of 
  the dot. Here's how it looks: `{{$.Site.Title}}`. See [Use $ to access the global context](https://gohugo.io/templates/introduction/#2-use--to-access-the-global-context)

See the result at `/public/blog/index.html`:

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

## Non-Hugo-specific variables are accessed via `.Params`

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

## Declare a template variable with `:=`, change its value with `=`

For convenience during template writing, you can declare internal variables with:

```go-template-html
{{ $a := "hello" }}
{{ $a = "HELLO" }}
{{ $a }}
```

In the first line, $a is declared and set to "hello". Then, it changes its value to "HELLO". Finally, it's printed on the template. 

## Two pitfalls with template variables

It's an error to use `=` to a variable that hasn't been `:=`'d before. 
Another common error is to use `:=` twice for the same name in different contexts: 

```go-template-html
{{ $a := 0 }}
{{ range (slice 1 2 3) }}
  {{ $a := . }}
  {{ $a }}
{{ end }}
{{ a }}
```
The result here is 0, instead of the expected 3. The reason is that `$a` is declared in the normal context, and then another, _different_ `$a` gets declared in the context of the range.
The third line should be changed to `$a = .`

It's difficult to understand when you start with Hugo, the difference is subtle and it's very difficult to search in the documentation. I just hope that you never run into this.

## Handling missing values with `if`, `with`, and `default`

The previous example is a bit fragile, because the templates are called using many different content files. If `my_custom_variable` doesn't exist in one of them, the whole build fails.

Here are three methods to avoid that: 

* `if`: This example is just to show how `if`-`else` works. For this it's sufficient to know that the `isset` function returns `true` or `false`. See [the documentation for `isset`]((https://gohugo.io/functions/isset)) if you want.
  ```go-template-html
  {{ if (isset .Params "my_custom_variable") }}
     <p> The value is: {{ .Param.my_custom_variable }} </p>
  {{ end }}
  ```
* `with`: The block is run if `.Params.my_custom_param` is set, and **not** run if it's
  missing. `with` rebinds the context: inside the block, the dot means "the variable", in this case "my_custom_param".
  ```go-template-html
  {{ with .Params.my_custom_param }}
    <p> The value is: {{.}} </p>
  {{ end }}
  ```
* [`default`](https://gohugo.io/functions/default/) : This is a very common idiom to set defaults.
  ```go-template-html
  {{ default "a default value just in case" .Param.my_custom_variable }}
  ```

## As usual, parenthesis clarify how the functions are applied. 
If a long sequence of functions need to be applied, parenthesis are used to disambiguate the order

```go-template-html
{{ upper "hello" }}
```

## The pipe operator `|` can save us many parenthesis.

As in unix, the pipe operator 
