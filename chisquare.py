<<<<<<< HEAD



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>si_spring_2015/chisquare.py at master · JasonJWilliamsNY/si_spring_2015 · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="JasonJWilliamsNY/si_spring_2015" name="twitter:title" /><meta content="si_spring_2015 - Science Institute Spring 2015" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/7266775?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/7266775?v=3&amp;s=400" property="og:image" /><meta content="JasonJWilliamsNY/si_spring_2015" property="og:title" /><meta content="https://github.com/JasonJWilliamsNY/si_spring_2015" property="og:url" /><meta content="si_spring_2015 - Science Institute Spring 2015" property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    
    <meta name="pjax-timeout" content="1000">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="46D04957:788B:8937BE:54FE2307" name="octolytics-dimension-request_id" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="Z7nfSp9HwpnpgdFkOYxUjHOl1J9Gw+kp5SJtH6G/Am6qjxBS6d6xWmzSWbRnjAXVG+g5Q6mh0BBM3F/Ls/QgWg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-928d6711d0e2b8553a8ad09c40303249229e43320d9ebd7fa17e5a3947767863.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-f7b433bc33c282aac87e7b77ece5fbc6ed8c3b4eec3368b74a9b449c2add2d6e.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="dd2aec6b591c5b14f9d3ad79ef61997e">

      
  <meta name="description" content="si_spring_2015 - Science Institute Spring 2015">
  <meta name="go-import" content="github.com/JasonJWilliamsNY/si_spring_2015 git https://github.com/JasonJWilliamsNY/si_spring_2015.git">

  <meta content="7266775" name="octolytics-dimension-user_id" /><meta content="JasonJWilliamsNY" name="octolytics-dimension-user_login" /><meta content="31919511" name="octolytics-dimension-repository_id" /><meta content="JasonJWilliamsNY/si_spring_2015" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="31919511" name="octolytics-dimension-repository_network_root_id" /><meta content="JasonJWilliamsNY/si_spring_2015" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/JasonJWilliamsNY/si_spring_2015/commits/master.atom" rel="alternate" title="Recent Commits to si_spring_2015:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


        
        <div class="header header-logged-out" role="banner">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions" role="navigation">
        <a class="button primary" href="/join" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      <a class="button" href="/login?return_to=%2FJasonJWilliamsNY%2Fsi_spring_2015%2Fblob%2Fmaster%2Fchisquare.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
    </div>

    <div class="site-search repo-scope js-site-search" role="search">
      <form accept-charset="UTF-8" action="/JasonJWilliamsNY/si_spring_2015/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/JasonJWilliamsNY/si_spring_2015/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
    </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item">
            <a class="header-nav-link" href="/explore" data-ga-click="(Logged out) Header, go to explore, text:explore">Explore</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/features" data-ga-click="(Logged out) Header, go to features, text:features">Features</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://enterprise.github.com/" data-ga-click="(Logged out) Header, go to enterprise, text:enterprise">Enterprise</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="(Logged out) Header, go to blog, text:blog">Blog</a>
          </li>
      </ul>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2FJasonJWilliamsNY%2Fsi_spring_2015"
    class="minibutton with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <span class="octicon octicon-eye"></span>
    Watch
  </a>
  <a class="social-count" href="/JasonJWilliamsNY/si_spring_2015/watchers">
    1
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2FJasonJWilliamsNY%2Fsi_spring_2015"
    class="minibutton with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/JasonJWilliamsNY/si_spring_2015/stargazers">
      0
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2FJasonJWilliamsNY%2Fsi_spring_2015"
        class="minibutton with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/JasonJWilliamsNY/si_spring_2015/network" class="social-count">
        0
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/JasonJWilliamsNY" class="url fn" itemprop="url" rel="author"><span itemprop="title">JasonJWilliamsNY</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/JasonJWilliamsNY/si_spring_2015" class="js-current-repository" data-pjax="#js-repo-pjax-container">si_spring_2015</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/JasonJWilliamsNY/si_spring_2015/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/JasonJWilliamsNY/si_spring_2015" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /JasonJWilliamsNY/si_spring_2015">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/JasonJWilliamsNY/si_spring_2015/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /JasonJWilliamsNY/si_spring_2015/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/JasonJWilliamsNY/si_spring_2015/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /JasonJWilliamsNY/si_spring_2015/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/JasonJWilliamsNY/si_spring_2015/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /JasonJWilliamsNY/si_spring_2015/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/JasonJWilliamsNY/si_spring_2015/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /JasonJWilliamsNY/si_spring_2015/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/JasonJWilliamsNY/si_spring_2015.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/JasonJWilliamsNY/si_spring_2015" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a> or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/JasonJWilliamsNY/si_spring_2015/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of JasonJWilliamsNY/si_spring_2015 as a zip file"
                   title="Download the contents of JasonJWilliamsNY/si_spring_2015 as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/JasonJWilliamsNY/si_spring_2015/blob/20949dad4dee6bc929500815a3f9f33c595b3092/chisquare.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:30d4c72728422dcab879d3ef8c3bfe05 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/JasonJWilliamsNY/si_spring_2015/blob/master/chisquare.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/JasonJWilliamsNY/si_spring_2015/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/JasonJWilliamsNY/si_spring_2015" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">si_spring_2015</span></a></span></span><span class="separator">/</span><strong class="final-path">chisquare.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="JasonJWilliamsNY" class="avatar" data-user="7266775" height="24" src="https://avatars2.githubusercontent.com/u/7266775?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/JasonJWilliamsNY" rel="author">JasonJWilliamsNY</a></span>
        <time datetime="2015-03-09T19:59:46Z" is="relative-time">Mar 9, 2015</time>
        <div class="commit-title">
            <a href="/JasonJWilliamsNY/si_spring_2015/commit/fffe001f79a22b4e5398c6bb3b88ce28b8fc2b34" class="message" data-pjax="true" title="added example">added example</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="JasonJWilliamsNY" data-user="7266775" height="24" src="https://avatars2.githubusercontent.com/u/7266775?v=3&amp;s=48" width="24" />
            <a href="/JasonJWilliamsNY">JasonJWilliamsNY</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">
      <div class="button-group">
        <a href="/JasonJWilliamsNY/si_spring_2015/raw/master/chisquare.py" class="minibutton " id="raw-url">Raw</a>
          <a href="/JasonJWilliamsNY/si_spring_2015/blame/master/chisquare.py" class="minibutton js-update-url-with-hash">Blame</a>
        <a href="/JasonJWilliamsNY/si_spring_2015/commits/master/chisquare.py" class="minibutton " rel="nofollow">History</a>
      </div><!-- /.button-group -->


          <a class="octicon-button disabled tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes"><span class="octicon octicon-pencil"></span></a>

        <a class="octicon-button danger disabled tooltipped tooltipped-w" href="#"
           aria-label="You must be signed in to make or propose changes">
      </a>
    </div><!-- /.actions -->
    <div class="file-info">
        50 lines (35 sloc)
        <span class="file-info-divider"></span>
      1.37 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c"># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-s1">Created on Mon Mar  9 14:56:19 2015</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-s1"></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-s1">@author: jasonwilliams</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-c">#import some special pyton functions</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-k">from</span> scipy <span class="pl-k">import</span> stats <span class="pl-k">as</span> sp</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line"><span class="pl-c">#Create a dictionary to hold the observations</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">observed_mnm <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line"><span class="pl-c"># Ask the user about each color and store the input</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Brown<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span>  <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Brown M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Blue<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span>   <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Blue M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Red<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span>    <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Red M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Orange<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span> <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Orange M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Yellow<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span> <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Yellow M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">observed_mnm[<span class="pl-s1"><span class="pl-pds">&#39;</span>Green<span class="pl-pds">&#39;</span></span>]<span class="pl-k">=</span>  <span class="pl-s3">float</span>(<span class="pl-s3">raw_input</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>How many Green M&amp;Ms? <span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line"><span class="pl-c">#turn the observed_mnm dictionary into a dataframe so we can do math</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line">data <span class="pl-k">=</span> pd.DataFrame.from_dict(observed_mnm, <span class="pl-vpf">orient</span> <span class="pl-k">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>index<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line"><span class="pl-c"># add the name &#39;observed&#39; to the dataframe</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">data.columns <span class="pl-k">=</span> [<span class="pl-s1"><span class="pl-pds">&#39;</span>observed<span class="pl-pds">&#39;</span></span>] </td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line"><span class="pl-c"># convert the observations to percentages</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">data <span class="pl-k">=</span> data <span class="pl-k">/</span> data.sum()</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line"><span class="pl-c"># add an &#39;expected&#39; column and fill in with </span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">data[<span class="pl-s1"><span class="pl-pds">&#39;</span>expected<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Blue<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.24</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Brown<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.13</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Green<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.16</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Yellow<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.14</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Red<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.13</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">data.expected[<span class="pl-s1"><span class="pl-pds">&#39;</span>Orange<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">0.20</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line"><span class="pl-k">print</span> data</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line"><span class="pl-c"># Use the stats package to do the ChiSquare test</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">result <span class="pl-k">=</span> sp.stats.chisquare(data.observation,data.expected,<span class="pl-vpf">ddof</span><span class="pl-k">=</span><span class="pl-c1">4</span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line"><span class="pl-k">print</span> result</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="http://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="http://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.03812s from github-fe129-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-4bf9533935259bb898a8d60e1958f4d047968c430eae889800a187e279faf38f.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-9d83860b0798bdd794d00b491fc7cb4ab9ea416cc8c511f719e253faa86e635b.js"></script>
      
      

  </body>
</html>

=======
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 9 14:56:19 2015
@author: jasonwilliams
"""
#import some special pyton functions
import pandas as pd

import scipy.stats.mstats as mst

#Create a dictionary to hold the observations
observed_mnm = {}
# Ask the user about each color and store the input
observed_mnm['Brown']   =  float(raw_input('How many Brown M&Ms? \n'))
observed_mnm['Blue']    =  float(raw_input('How many Blue M&Ms? \n'))
observed_mnm['Red']     =  float(raw_input('How many Red M&Ms? \n'))
observed_mnm['Orange']  =  float(raw_input('How many Orange M&Ms? \n'))
observed_mnm['Yellow']  =  float(raw_input('How many Yellow M&Ms? \n'))
observed_mnm['Green']   =  float(raw_input('How many Green M&Ms? \n'))
#turn the observed_mnm dictionary into a dataframe so we can do math
data = pd.DataFrame.from_dict(observed_mnm, orient ='index')
# add the name 'observed' to the dataframe
data.columns = ['observed']
# sum up the observations
observations = data.observed.sum()

# convert the observations to percentages
#data = data / data.sum()
# add an 'expected' column and fill in with
data['expected'] = ''
data.expected['Blue']   = 0.24  * observations
data.expected['Brown']  = 0.13  * observations
data.expected['Green']  = 0.16  * observations
data.expected['Yellow'] = 0.14  * observations
data.expected['Red']    = 0.13  * observations
data.expected['Orange'] = 0.20  * observations
print data
# Use the stats package to do the ChiSquare test
result = mst.chisquare(data.observed,data.expected)
print "Chi-squared statistic is %f" %result[0]
print "p-value is: %f" %result[1]
print "Probability null hypothesis is true: %f%%" %(float(result[1])*100)


if  (float(result[1])*100) > 5:
    print "You should accept the null hypthothesis!"
else:
    print "You should reject the null hypthothesis!"
>>>>>>> 11ac
