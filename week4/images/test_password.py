<!DOCTYPE html>
<!-- saved from url=(0065)https://byui-cse.github.io/cse111-ww-course/week03/prepare-1.html -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CSE 111 | Learning Activities</title>
  <link rel="preconnect" href="https://fonts.googleapis.com/">
  <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">
  <link href="./test_password_files/css2" rel="stylesheet">
  <link rel="stylesheet" href="./test_password_files/course.css">
  <link rel="stylesheet" href="./test_password_files/math.css">
  <link rel="stylesheet" href="./test_password_files/vs2015.min.css">
  <script type="text/javascript" src="./test_password_files/620f7e0f8d21af1a_complete.js.download" crossorigin="anonymous"></script>
<style type="text/css">.hljs-ln{border-collapse:collapse}.hljs-ln td{padding:0}.hljs-ln-n:before{content:attr(data-line-number)}</style></head>

<body>
  <header>
    <div class="page">
      <h1>CSE 111<span id="coursetitle">: Programming with Functions</span></h1>
      <img src="./test_password_files/byui-logo.svg" alt="BYU-I logo" class="logo">
    </div>
  </header>
  <main class="page">
    <nav id="autogen-top-nav">
      <!-- This nav is auto-generated -->
      <span><a href="https://byui-cse.github.io/cse111-ww-course/index.html">Home</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week01/index.html">W1</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week02/index.html">W2</a></span>
      <span class="active"><a href="https://byui-cse.github.io/cse111-ww-course/week03/index.html">W3</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week04/index.html">W4</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week05/index.html">W5</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week06/index.html">W6</a></span>
      <span><a href="https://byui-cse.github.io/cse111-ww-course/week07/index.html">W7</a></span>
      <!-- end auto-generated -->
    </nav>
    <h2>W03 Learning Activity (1 of 2): Testing Functions</h2>
    <p>During this lesson, you will learn to use a more systematic
      approach to developing code. Specifically, you will learn how to
      write test functions that automatically verify that program
      functions are correct. You will learn how to use a Python module
      named <code>pytest</code> to run your test functions, and you will
      learn how to read the output of <code>pytest</code> to help you find
      and fix mistakes in your code.</p>
    <h3 id="concepts">Concepts</h3>
    <p>Here are the Python programming concepts and topics that you
      should learn during this lesson:</p>
    <h4 id="ineff_test">Inefficient Testing</h4>
    <p>During previous lessons, you tested your programs by running
      them, typing user input, reading the program’s output, and verifying
      that the output was correct. This is a valid way to test a program.
      However, it is time consuming, tedious, and error prone. A much
      better way to test a program is to test its functions individually
      and to write separate <dfn>test functions</dfn> that
      <em>automatically</em> verify that the program’s functions are
      correct.
    </p>
    <p>In this course, you will write test functions in a Python file
      that is separate from your Python program. In other words, you will
      keep normal program code and test code in separate
      files.</p>
    <h4 id="assert">Assert Statements</h4>
    <p>In a computer program, an <dfn>assertion</dfn> is a statement
      that causes the computer to check if a comparison is true. When the
      computer checks the comparison, if the comparison is true, the
      computer will continue to execute the code in the program. However,
      if the comparison is false, the computer will raise an
      <code>AssertionError</code>, which will likely cause the program to
      terminate. (In <a href="https://byui-cse.github.io/cse111-ww-course/week05/prepare-2.html">Week 05</a>
      you will learn how to write code to handle errors so that a program
      won’t terminate when the computer raises an error.)
    </p>
    <p>A programmer writes assertions in a program to inform the
      computer of comparisons that must be true in order for the program
      to run successfully. The Python keyword to write an assertion is
      <a href="https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement"><code>assert</code></a>.
      Imagine a program used by a bank to track account balances,
      deposits, and withdrawals. A programmer might write the first few
      lines of the <code>deposit</code> function like this:
    </p>
    <div id="ex1">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-keyword">def</span> <span class="hljs-title function_">deposit</span>(<span class="hljs-params">amount</span>):</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2">  <span class="hljs-comment"># In order for this program to work correctly and</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">  <span class="hljs-comment"># for the bank records to be correct, we must not</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4">  <span class="hljs-comment"># allow someone to deposit a zero or negative amount.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5">  <span class="hljs-keyword">assert</span> amount &gt; <span class="hljs-number">0</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6">    ⋮</td></tr></tbody></table></code></pre>
    </div>
    <p>The <code>assert</code> statement at
      line&nbsp;5 in the
      previous example will cause the computer to check if the
      <var>amount</var> is greater than zero (0). If the <var>amount</var>
      is greater than zero, the computer will continue to execute the
      program. However, if the <var>amount</var> is zero or less
      (negative), the computer will raise an <code>AssertionError</code>,
      which will likely cause the program to terminate.
    </p>
    <p>A programmer can write any valid Python comparison in an
      <code>assert</code> statement. Here are a few examples from various
      unrelated programs:
    </p>
    <div id="ex2">
      <pre><code class="language-python nohljsln hljs" data-highlighted="yes"><span class="hljs-keyword">assert</span> temperature &lt; <span class="hljs-number">0</span>
<span class="hljs-keyword">assert</span> <span class="hljs-built_in">len</span>(given_name) &gt; <span class="hljs-number">0</span>
<span class="hljs-keyword">assert</span> balance == <span class="hljs-number">0</span>
<span class="hljs-keyword">assert</span> school_year != <span class="hljs-string">"senior"</span>
</code></pre>
    </div>
    <h4 id="pytest">The pytest Module</h4>
    <p><a href="https://docs.pytest.org/en/latest/reference/reference.html"><code>pytest</code></a>
      is a third-party Python module that makes it easy to write and run
      test functions. There are other Python testing modules besides
      <code>pytest</code>, but <code>pytest</code> seems to be the easiest
      to use. <code>pytest</code> is not a standard Python module. It is a
      third-party module. This means that when you installed Python on
      your computer, <code>pytest</code> was not installed, and you will
      need to install <code>pytest</code> in order to use it. During the
      checkpoint of this lesson, you will use a standard Python module
      named <code>pip</code> to install <code>pytest</code>.
    </p>
    <p><code>pytest</code> allows a programmer to write simple test
      functions. The name of each test function should begin with "test_",
      and each test function should use the Python <code>assert</code>
      statement to verify that a program function returns a correct
      result. For example, if we want to verify that the built-in
      <code>min</code> function works correctly, we could write a test
      function like this:</p>
    <div id="ex3">
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-keyword">def</span> <span class="hljs-title function_">test_min</span>():</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2">  <span class="hljs-keyword">assert</span> <span class="hljs-built_in">min</span>(<span class="hljs-number">7</span>, -<span class="hljs-number">3</span>, <span class="hljs-number">0</span>, <span class="hljs-number">2</span>) == -<span class="hljs-number">3</span></td></tr></tbody></table></code></pre>
    </div>
    <p>In the previous test function, the <code>assert</code> statement will
      cause the computer to first call the <code>min</code> function and
      pass 7, −3, 0, and 2 as arguments to the <code>min</code>
      function. The <code>min</code> function will find the minimum value
      of its parameters and return that minimum value. Then the
      <code>assert</code> statement will compare the returned minimum
      value to −3. If the returned value is not −3, the
      <code>assert</code> statement will raise an exception which will
      cause <code>pytest</code> to print an error message.
    </p>
    <h4 id="compare_floats">Comparing Floating Point Numbers</h4>
    <p>Within a computer’s memory, everything (all numbers, text, sound,
      pictures, movies, everything) is stored using the binary number
      system. While executing a Python program, a computer stores integers
      in binary in a way that exactly represents the integers. For
      example, a computer stores the integer 23 as 00010111 in binary
      which is an exact representation of decimal 23. However, a computer
      approximates floating-point numbers (numbers with digits after the
      decimal place). For example, while executing a Python program, a
      computer stores the floating-point number 23.7 as binary
      0100000000110111101100110011001100110011001100110011001100110011.
      This binary number is actually 23.69999999999999928945726424 in
      decimal which is an approximation to 23.7</p>
    <p>Because computers approximate floating-point numbers, we must
      carefully compare them in our test functions. It is a bad practice
      to check if floating-point numbers are equal using just the equality
      operator (==). A better way to compare two floating-point numbers is
      to subtract them and check if their difference is small as shown at
      line&nbsp;6 of
      example&nbsp;4.
    </p>
    <div id="ex4">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Example 4</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-comment"># The variables e and f can be any floating-</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3"><span class="hljs-comment"># point numbers from any calculation.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4">e = <span class="hljs-number">7.135</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5">f = <span class="hljs-number">7.128</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6"><span class="hljs-keyword">if</span> <span class="hljs-built_in">abs</span>(e - f) &lt; <span class="hljs-number">0.01</span>:</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="7"><div class="hljs-ln-n" data-line-number="7"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="7">    <span class="hljs-built_in">print</span>(<span class="hljs-string">f"<span class="hljs-subst">{e}</span> and <span class="hljs-subst">{f}</span> are close enough so"</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="8"><div class="hljs-ln-n" data-line-number="8"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="8">    <span class="hljs-built_in">print</span>(<span class="hljs-string">"we'll consider them to be equal."</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="9"><div class="hljs-ln-n" data-line-number="9"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="9"><span class="hljs-keyword">else</span>:</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="10"><div class="hljs-ln-n" data-line-number="10"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="10">    <span class="hljs-built_in">print</span>(<span class="hljs-string">f"<span class="hljs-subst">{e}</span> and <span class="hljs-subst">{f}</span> are not close and"</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="11"><div class="hljs-ln-n" data-line-number="11"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="11">    <span class="hljs-built_in">print</span>(<span class="hljs-string">"therefor not equal."</span>)</td></tr></tbody></table></code></pre>
    </div>
    <p>In example&nbsp;4 at
      line&nbsp;6, if the
      difference between <var>e</var> and <var>f</var> is less than 0.01,
      the computer will consider the two numbers to be equal. The number
      0.01 in the comparison at
      line&nbsp;6 is called the
      tolerance. The <dfn>tolerance</dfn> is the maximum difference
      between two floating-point numbers that the programmer will allow
      and still consider the numbers to be equal.
    </p>
    <h4 id="approx"><code>approx</code> Function</h4>
    <p>The comparison in example&nbsp;4 at
      line&nbsp;6 is a little
      tedious to write and read. Also, choosing the tolerance is sometimes
      difficult. The <code>pytest</code> module contains a function named
      <code>approx</code> to help us compare floating-point numbers more
      easily. The
      <a href="https://docs.pytest.org/en/latest/reference/reference.html#pytest-approx"><code>approx</code> function</a><sup>*</sup>
      compares two floating-point numbers and returns <code>True</code> if
      they are equal within an appropriate tolerance.
    </p>
    <ul class="notes">
      <li><code>approx</code> is not a function. It is a Python class.
        Because CSE&nbsp;111 students have not yet learned about
        classes, this document refers to <code>approx</code> as a
        function. For the purposes of CSE&nbsp;111, it is sufficient for
        students to think of <code>approx</code> as a function.</li>
    </ul>
    <p>The <code>approx</code> function has the following function
      header:</p>
    <div>
      <pre><code class="language-python hljs" data-highlighted="yes"><span class="hljs-keyword">def</span> <span class="hljs-title function_">approx</span>(<span class="hljs-params">expected_value, rel=<span class="hljs-literal">None</span>, <span class="hljs-built_in">abs</span>=<span class="hljs-literal">None</span>, nan_ok=<span class="hljs-literal">False</span></span>)</code></pre>
    </div>
    <p>Notice that the last three parameters of the <code>approx</code>
      function have default values: <code>rel=None, abs=None,
    nan_ok=False</code>. Because they have default values, when we call
      <code>approx</code>, we’re not required to pass arguments for the
      last three parameters. In other words in a test function, we can
      call <code>approx</code> like this:
    </p><div>
      <pre><code class="language-python nohljsln hljs" data-highlighted="yes"><span class="hljs-keyword">def</span> <span class="hljs-title function_">test_function</span>():
  <span class="hljs-keyword">assert</span> actual_value == approx(expected_value)</code></pre>
    </div>
    <p>If we call <code>approx</code> with just one argument,
      <code>approx</code> will compare the actual value and expected value
      and return <code>True</code> if the difference between the two
      values is less than one millionth of the expected value. In other
      words, one millionth of the expected value (expected_value /
    1000000) is the default tolerance. Sometimes this is not the right
    tolerance. The <code>approx</code> function has two parameters,
    <code>rel</code> and <code>abs</code>, that we can use to give
    <code>approx</code> a better tolerance to use in its comparison. For
    example, to test the <code>math.sqrt</code> function, we could write
    a test function like this:
    </p>
    <div id="ex5">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Example 5</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-keyword">def</span> <span class="hljs-title function_">test_sqrt</span>():</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">  <span class="hljs-keyword">assert</span> math.sqrt(<span class="hljs-number">5</span>) == approx(<span class="hljs-number">2.24</span>, rel=<span class="hljs-number">0.01</span>)</td></tr></tbody></table></code></pre>
    </div>
    <p>Notice the <code>rel</code> named argument in
      line&nbsp;3 of the
      previous example. The <code>rel</code> named argument causes the
      <code>approx</code> function to compute the tolerance relative to
      the expected value. This means that the <code>assert</code>
      statement and the <code>approx</code> function at line&nbsp;3 in the
      previous example cause the computer to verify that the actual value
      returned from <code>math.sqrt(5)</code> is within 1%&nbsp;(0.01) of
      2.24. When a programmer uses the <code>rel</code> named argument,
      the <code>approx</code> function uses code similar to example&nbsp;6
      to determine if the actual and expected values are equal.
    </p>
    <div id="ex6">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Example 6</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-comment"># Compute the tolerance.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">tolerance = expected_value * rel</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4"><span class="hljs-comment"># Use the tolerance to determine if the actual</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5"><span class="hljs-comment"># and expected values are close enough to be</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6"><span class="hljs-comment"># considered equal.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="7"><div class="hljs-ln-n" data-line-number="7"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="7"><span class="hljs-keyword">if</span> <span class="hljs-built_in">abs</span>(actual_value - expected_value) &lt; tolerance:</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="8"><div class="hljs-ln-n" data-line-number="8"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="8">    <span class="hljs-keyword">return</span> <span class="hljs-literal">True</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="9"><div class="hljs-ln-n" data-line-number="9"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="9"><span class="hljs-keyword">else</span>:</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="10"><div class="hljs-ln-n" data-line-number="10"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="10">    <span class="hljs-keyword">return</span> <span class="hljs-literal">False</span></td></tr></tbody></table></code></pre>
    </div>
    <p>From lines&nbsp;3
        and&nbsp;7 of example&nbsp;6, we learn that
      <code>approx</code> will return <code>True</code> if the difference
      between the actual value returned from <code>math.sqrt(5)</code> and
      the expected value is less than 0.0224 (2.24&nbsp;*&nbsp;0.01).
    </p>
    <p>We can also use the <code>abs</code> named argument to give
      <code>approx</code> a tolerance. We can write a test for the
      <code>math.sqrt</code> function like this:
    </p>
    <div id="ex7">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Example 7</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-keyword">def</span> <span class="hljs-title function_">test_sqrt</span>():</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">    <span class="hljs-keyword">assert</span> math.sqrt(<span class="hljs-number">5</span>) == approx(<span class="hljs-number">2.24</span>, <span class="hljs-built_in">abs</span>=<span class="hljs-number">0.01</span>)</td></tr></tbody></table></code></pre>
    </div>
    <p>Notice the <code>abs</code> named argument in
      line&nbsp;3 of the
      previous example. The <code>abs</code> named argument causes
      the <code>approx</code> function to return <code>True</code> if the
      difference between the actual and expected values is less than the
      number in <code>abs</code> (0.01 in the previous example). This is
      different from the <code>rel</code> named argument which causes
      approx to return <code>True</code> if the difference is less than
      <code>rel * expected_value</code>. The <code>abs</code> named
      argument is simpler and easier to understand than the
      <code>rel</code> named argument.
    </p>
    <h4 id="test_func">How to Test a Function</h4>
    <p>To test a function you should do the following:</p>
    <ol>
      <li>
        <div>Write a function that is part of your normal Python
          program.</div>
      </li>
      <li>
        <div>Think about different parameter values that will cause
          the computer to execute all the code in your function and will
          possibly cause your function to fail or return an incorrect
          result.</div>
      </li>
      <li>
        <div>In a separate Python file, write a test function that
          calls your program function and uses an <code>assert</code>
          statement to <em>automatically</em> verify that the value
          returned from your program function is correct.</div>
      </li>
      <li>
        <div>Use <code>pytest</code> to run the test
          function.</div>
      </li>
      <li>
        <div>Read the output of <code>pytest</code> and use that
          output to help you find and fix mistakes in both your program
          function and test function.</div>
      </li>
    </ol>
    <h5 id="example">Example</h5>
    <p>Below is a simple function named <code>cels_from_fahr</code> that
      converts a temperature in Fahrenheit to Celsius and returns the
      Celsius temperature. The <code>cels_from_fahr</code> function is
      part of a larger Python program in a file named
      <code>weather.py</code>.
    </p>
    <div id="ex8">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># weather.py</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-keyword">def</span> <span class="hljs-title function_">cels_from_fahr</span>(<span class="hljs-params">fahr</span>):</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">  <span class="hljs-string"><span class="hljs-string">"""Convert a temperature in Fahrenheit to</span></span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4"><span class="hljs-string">  Celsius and return the Celsius temperature.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5"><span class="hljs-string">  """</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6">  cels = (fahr - <span class="hljs-number">32</span>) * <span class="hljs-number">5</span> / <span class="hljs-number">9</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="7"><div class="hljs-ln-n" data-line-number="7"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="7">  <span class="hljs-keyword">return</span> cels</td></tr></tbody></table></code></pre>
    </div>
    <p>We want to test the <code>cels_from_fahr</code> function. From
      the function header at
      line&nbsp;2 in
      <code>weather.py</code>, we see that <code>cels_from_fahr</code>
      takes one parameter named <var>fahr</var>. To adequately test this
      function, we should call it at least three times with the following
      arguments.
    </p>
    <ul>
      <li>
        <div>a negative number</div>
      </li>
      <li>
        <div>zero</div>
      </li>
      <li>
        <div>a positive number</div>
      </li>
    </ul>
    <p>In a separate file named <code>test_weather.py</code> we write a
      test function named <code>test_cels_from_fahr</code> as follows:</p>
    <div id="ex9">
      
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># test_weather.py</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-keyword">from</span> weather <span class="hljs-keyword">import</span> cels_from_fahr</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3"><span class="hljs-keyword">from</span> pytest <span class="hljs-keyword">import</span> approx</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4"><span class="hljs-keyword">import</span> pytest</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5"><span class="hljs-keyword">def</span> <span class="hljs-title function_">test_cels_from_fahr</span>():</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6">    <span class="hljs-string"><span class="hljs-string">"""Test the cels_from_fahr function by calling it and</span></span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="7"><div class="hljs-ln-n" data-line-number="7"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="7"><span class="hljs-string">    comparing the values it returns to the expected values.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="8"><div class="hljs-ln-n" data-line-number="8"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="8"><span class="hljs-string">    Notice this test function uses pytest.approx to compare</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="9"><div class="hljs-ln-n" data-line-number="9"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="9"><span class="hljs-string">    floating-point numbers.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="10"><div class="hljs-ln-n" data-line-number="10"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="10"><span class="hljs-string">    """</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="11"><div class="hljs-ln-n" data-line-number="11"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="11">    <span class="hljs-keyword">assert</span> cels_from_fahr(-<span class="hljs-number">25</span>) == approx(-<span class="hljs-number">31.66667</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="12"><div class="hljs-ln-n" data-line-number="12"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="12">    <span class="hljs-keyword">assert</span> cels_from_fahr(<span class="hljs-number">0</span>) == approx(-<span class="hljs-number">17.77778</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="13"><div class="hljs-ln-n" data-line-number="13"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="13">    <span class="hljs-keyword">assert</span> cels_from_fahr(<span class="hljs-number">32</span>) == approx(<span class="hljs-number">0</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="14"><div class="hljs-ln-n" data-line-number="14"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="14">    <span class="hljs-keyword">assert</span> cels_from_fahr(<span class="hljs-number">70</span>) == approx(<span class="hljs-number">21.1111</span>)</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="15"><div class="hljs-ln-n" data-line-number="15"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="15"><span class="hljs-comment"># Call the main function that is part of pytest so that the</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="16"><div class="hljs-ln-n" data-line-number="16"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="16"><span class="hljs-comment"># computer will execute the test functions in this file.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="17"><div class="hljs-ln-n" data-line-number="17"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="17">pytest.main([<span class="hljs-string">"-v"</span>, <span class="hljs-string">"--tb=line"</span>, <span class="hljs-string">"-rN"</span>, __file__])</td></tr></tbody></table></code></pre>
    </div>
    <p>Notice in <code>test_weather.py</code> at
      lines&nbsp;11–14
      that the test function <code>test_cels_from_fahr</code> calls the
      program function <code>cels_from_fahr</code> four times: once with a
      negative number, once with zero, and twice with positive numbers.
      Notice also that the test function uses <code>assert</code> and
      <code>approx</code>.
    </p>
    <p>After writing the test function, we use <code>pytest</code> to
      run the test function. At
      line&nbsp;17,
      instead of writing a call to the <code>main</code> function, as we
      do in program files, we write a call to the <code>pytest.main</code>
      function. In CSE&nbsp;111, at the bottom of all test files, we will
      write a call to <code>pytest.main</code> exactly as shown in
      line&nbsp;17. This call to
      <code>pytest.main</code> will cause the <code>pytest</code> module
      to run all the test functions in the <code>test_weather.py</code>
    file. When <code>pytest</code> runs the test functions, it will
    produce output that tells us if the tests passed or failed like
    this:
    </p>
    <pre class="console">&gt; python test_weather.py
===================== test session starts ======================
platform win32--Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.1
rootdir: C:\Users\cse111\week3
collected 1 item
test_weather.py::test_cels_from_fahr <span class="pass">PASSED               [100%]</span>
<span class="pass">====================== 1 passed in 0.10s =======================</span></pre>
    <p>As shown above, <code>pytest</code> runs the
      <code>test_cels_from_fahr</code> function which calls the
      <code>cels_from_fahr</code> function four times and verifies that
      <code>cels_from_fahr</code> returns the correct value each time. We
      can see from the output of <code>pytest</code>, "PASSED [100%]" and
      "1&nbsp;passed", that the <code>cels_from_fahr</code> function
      returned the expected (correct) result all four times.
    </p>
    <h4 id="separate">Separating Program Code from Test Code</h4>
    <p>In CSE&nbsp;111, we will write test functions in a file separate
      from program functions. It is a good idea to separate test functions
      and program functions because the separation makes it easy to
      release a program to users without releasing the test functions to
      them. In general, users of a program don’t want the test functions.
      One consequence of writing program functions and test functions in
      separate files is that we must add an import statement at the top of
      the test file that imports all the program functions that will be
      tested.</p>
    <p>Line&nbsp;2 from
      <code>test_weather.py</code> above is an example of an import
      statement that imports functions from a program file. Line&nbsp;3
      matches this template:
    </p>
    <div>
      <pre><code class="language-python hljs" data-highlighted="yes"><span class="hljs-keyword">from</span> file_name <span class="hljs-keyword">import</span> function_1, function_2, … function_N
</code></pre>
    </div>
    <p>When the computer imports functions from a file, the computer
      immediately executes all statements that are not written inside a
      function. This includes the statement to call the <code>main</code>
      function:</p>
    <div>
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Start this program by</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-comment"># calling the main function.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">main()</td></tr></tbody></table></code></pre>
    </div>
    <p>This means that when we run our test functions, the computer will
      import our program functions and at the same time, will execute the
      call to <code>main()</code> which will start the program executing.
      However, we don’t want the computer to execute the program while it
      is executing the test functions, so we have a problem. How can we
      get the computer to import the program functions without executing
      the <code>main</code> function? Fortunately, the developers of
      Python gave us a solution to this problem. Instead of writing the
      following code to start our program running:</p>
    <div>
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># Start this program by</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-comment"># calling the main function.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3">main()</td></tr></tbody></table></code></pre>
    </div>
    <p>We write an <code>if</code> statement above the call to
      <code>main()</code> like this:
    </p>
    <div>
      <pre><code class="language-python hljs" data-highlighted="yes"><table class="hljs-ln"><tbody><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="1"><div class="hljs-ln-n" data-line-number="1"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="1"><span class="hljs-comment"># If this file is executed like this:</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="2"><div class="hljs-ln-n" data-line-number="2"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="2"><span class="hljs-comment"># &gt; python program.py</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="3"><div class="hljs-ln-n" data-line-number="3"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="3"><span class="hljs-comment"># then call the main function. However, if this file is simply</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="4"><div class="hljs-ln-n" data-line-number="4"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="4"><span class="hljs-comment"># imported (e.g. into a test file), then skip the call to main.</span></td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="5"><div class="hljs-ln-n" data-line-number="5"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="5"><span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">"__main__"</span>:</td></tr><tr><td class="hljs-ln-line hljs-ln-numbers" data-line-number="6"><div class="hljs-ln-n" data-line-number="6"></div></td><td class="hljs-ln-line hljs-ln-code" data-line-number="6">    main()</td></tr></tbody></table></code></pre>
    </div>
    <p>Writing the <code>if</code> statement above the call to
      <code>main()</code> is the correct way to write code to start a
      program. The Python programming language guarantees that when the
      computer imports the program functions (in order to test them), the
      comparison in the <code>if</code> statement will be false, so the
      computer will skip the call to <code>main()</code>. At another time,
      when the computer executes the program (not the test functions), the
      comparison in the <code>if</code> statement will be true, which will
      cause the computer to call the <code>main</code> function and start
      the program.
    </p>
    <h4 id="test_which_funcs">Which Program Functions Should We Test?</h4>
    <p>Because we are responsible computer programmers and want to
      ensure that all of our program functions work correctly, we would
      like to test all program functions. In other words, we would like to
      write at least one test function for each program function. However,
      this may not always be possible. The easiest program functions to
      test are the functions that have parameters and return a value. The
      hardest program functions to test are the functions that get user
      input, print results to a terminal window, or draw something to a
      window. During the next eight lessons in CSE&nbsp;111, we will
      usually write one test function for each program function that is
      easy to test, meaning each function that does not get user input and
      does not print to a terminal window. This means that you won’t write
      a test function for your program’s <code>main</code> function
      because <code>main</code> usually gets user input and prints to a
      terminal window.</p>
    <h3 id="video">Video</h3>
    <p>Watch the following video that shows a BYU-Idaho faculty member
      writing two test functions and using pytest to run them.</p>
    <div>
      <figure class="video-container"><iframe allowfullscreen="" title="Writing a Test Function" src="./test_password_files/1157612.html"></iframe>ifr<figcaption><a href="https://video.byui.edu/media/t/1_9ickss60">Writing a
            Test Function</a> <span class="duration">(20 minutes)</span></figcaption>
      </figure>
    </div>
    <h3 id="docs">Documentation</h3>
    <p>The official online documentation for <code>pytest</code>
      contains much more information about using <code>pytest</code>. The
      following pages are the most applicable to CSE&nbsp;111.</p>
    <ul class="references">
      <li>
        <div><a href="https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test">Create your first test</a></div>
      </li>
      <li>
        <div><a href="https://docs.pytest.org/en/latest/how-to/assert.html#asserting-with-the-assert-statement"><code>assert</code></a></div>
      </li>
      <li>
        <div><a href="https://docs.pytest.org/en/latest/reference/reference.html#pytest-approx"><code>pytest.approx</code></a></div>
      </li>
      <li>
        <div><a href="https://docs.pytest.org/en/latest/how-to/usage.html#calling-pytest-from-python-code"><code>pytest.main</code></a></div>
      </li>
    </ul>
    <h3 id="summary">Summary</h3>
    <p>During this lesson, you are learning to write test functions that
      automatically verify that program functions are working correctly.
      In CSE&nbsp;111, you will write test functions in a Python file that
      is separate from your program file. At the top of the test file, you
      will import the program functions. Then you will write one test
      function for each program function, except <code>main</code>. Within
      a test function, you will write <code>assert</code> statements that
      compare the value returned from a program function to the expected
      value. You will use a standard Python module named
      <code>pytest</code> to run your test functions. When a test fails,
      you will use the output of <code>pytest</code> to help you find and
      fix the mistakes in your code.
    </p>
  <h2>W03 Checkpoint: Testing Functions</h2>
  <h2 id="purpose">Purpose</h2>
  <p>Improve your ability to verify the correctness of functions by
    writing a test function and running it with <code>pytest</code>.</p>
  <hh3 id="assign">Assignment</hh3>
  <p>Write a test function that tests a previously written function.
    Then use <code>pytest</code> to run test functions.</p>
  <h3 id="helpful_docs">Helpful Documentation</h3>
  <ul class="mixed long">
    <li class="reference">
      <div><a href="https://docs.python.org/3/installing/index.html"><code>pip</code></a>
        is a standard Python module that you can use to download and
        install third-party modules. During the checkpoint of this
        lesson, you will use <code>pip</code> to download and install
        <code>pytest</code>, so that you can use <code>pytest</code> in
        your test code.
      </div>
    </li>
    <li class="video">
      <div>This
        <a href="https://video.byui.edu/media/t/1_f72kfav3">video about
          the <code>pip</code> module</a>
        <span class="duration">(16 minutes)</span> shows a BYU-Idaho
        faculty member using <code>pip</code> to install other Python
        modules.
      </div>
    </li>
  </ul>
  <h3 id="steps">Steps</h3>
  <p>Do the following:</p>
  <ol>
    <li>
      <div>Open a new terminal frame in VS Code by doing the
        following:
        <ol>
          <li>
            <div>Open VS Code</div>
          </li>
          <li>
            <div>On the menu bar for VS Code, click "Terminal"</div>
          </li>
          <li>
            <div>On the menu, click "New Terminal"</div>
          </li>
        </ol>
        <figure class="full">
          <img loading="lazy" src="./test_password_files/open_terminal.png" alt="A screenshot of VS Code showing how to open a terminal frame" title="A screenshot of VS Code showing how to open a terminal frame">
        </figure>
        <p>This will open a terminal frame at the bottom of the VS Code
          window. A terminal is a window or frame where a user can type
          and execute computer commands.</p>
        <figure class="full">
          <img loading="lazy" src="./test_password_files/terminal.png" alt="A screenshot of VS Code showing an open terminal frame" title="A screenshot of VS Code showing an open terminal frame">
        </figure>
      </div>
    </li>
    <li>
      <div>Copy and paste the following command into the terminal
        frame and execute the command by pressing the Enter key. This
        command will upgrade <code>pip</code> and several other parts of
        the Python installation modules so that <code>pip</code> will
        work correctly.
        <ul>
          <li>
            <div>Mac OS users:
              <pre class="console">python3 -m pip install --user --upgrade pip setuptools wheel</pre>
            </div>
          </li>
          <li>
            <div>Windows users:
              <pre class="console">python -m pip install --user --upgrade pip setuptools wheel</pre>
              <ul class="notes">
                <li>If your computer is running the Windows operating
                  system, and the above command doesn’t work on your
                  computer, try the <code>py</code> command instead of the
                  <code>python</code> command like this:
                </li>
              </ul>
              <pre class="console">py -m pip install --user --upgrade pip setuptools wheel</pre>
            </div>
          </li>
        </ul>
        <figure class="full">
          <img loading="lazy" src="./test_password_files/upgrade_pip.png" alt="A screenshot of VS Code showing the command to upgrade pip" title="A screenshot of VS Code showing the command to upgrade pip">
        </figure>
      </div>
    </li>
    <li>
      <div>Install the <code>pytest</code> module by copying,
        pasting, and executing the following command in the terminal
        frame.
        <ul>
          <li>
            <div>Mac OS users:
              <pre class="console">python3 -m pip install --user pytest</pre>
            </div>
          </li>
          <li>
            <div>Windows users:
              <pre class="console">python -m pip install --user pytest</pre>
              <ul class="notes">
                <li>If your computer is running the Windows operating
                  system, and the above command doesn’t work on your
                  computer, try the <code>py</code> command instead of the
                  <code>python</code> command like this:
                </li>
              </ul>
              <pre class="console">py -m pip install --user pytest</pre>
            </div>
          </li>
        </ul>
        <figure class="full">
          <img loading="lazy" src="./test_password_files/install_pytest.png" alt="A screen shot of VS Code showing the command to install pytest" title="A screen shot of VS Code showing the command to install pytest">
        </figure>
      </div>
    </li>
    <li>
      <div>Download these two Python files:
        <a download="" href="https://byui-cse.github.io/cse111-ww-course/week03/samples/words.py">words.py</a> and
        <a download="" href="https://byui-cse.github.io/cse111-ww-course/week03/samples/test_words.py">test_words.py</a>
        and save them in the same folder.
      </div>
    </li>
    <li>
      <div>Open the downloaded <code>words.py</code> file in VS
        Code. Notice the <code>words.py</code> file contains two small
        functions named <code>prefix</code> and <code>suffix</code>.
        Notice also that each function has a documentation string (a
        triple quoted string immediately below a function header) that
        describes what the function does. Read the documentation strings
        for both functions.</div>
    </li>
    <li>
      <div>Open the downloaded <code>test_words.py</code> file in
        VS Code. In <code>test_words.py</code> examine the
        <code>test_prefix</code> function. Notice that it takes no
        parameters and contains nine <code>assert</code> statements.
        Each assert statement calls the <code>prefix</code> function and
        then compares the value returned from the <code>prefix</code>
        function to the expected value.
      </div>
    </li>
    <li>
      <div>In <code>test_words.py</code> write a function named
        <code>test_suffix</code> that is similar to the
        <code>test_prefix</code> function. The <code>test_suffix</code>
        function should take no parameters and contain nine
        <code>assert</code> statements that call the <code>suffix</code>
        function with these parameters:
        <table class="center">
          <thead>
            <tr>
              <th colspan="2">Arguments</th>
              <th rowspan="2">Expected<br>Return<br>Value</th>
            </tr>
            <tr>
              <th>s1</th>
              <th>s2</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>""</td>
              <td>""</td>
              <td>""</td>
            </tr>
            <tr>
              <td>""</td>
              <td>"correct"</td>
              <td>""</td>
            </tr>
            <tr>
              <td>"clear"</td>
              <td>""</td>
              <td>""</td>
            </tr>
            <tr>
              <td>"angelic"</td>
              <td>"awesome"</td>
              <td>""</td>
            </tr>
            <tr>
              <td>"found"</td>
              <td>"profound"</td>
              <td>"found"</td>
            </tr>
            <tr>
              <td>"ditch"</td>
              <td>"itch"</td>
              <td>"itch"</td>
            </tr>
            <tr>
              <td>"happy"</td>
              <td>"funny"</td>
              <td>"y"</td>
            </tr>
            <tr>
              <td>"tired"</td>
              <td>"fatigued"</td>
              <td>"ed"</td>
            </tr>
            <tr>
              <td>"swimming"</td>
              <td>"FLYING"</td>
              <td>"ing"</td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
    <li>
      <div>Save your <code>test_words.py</code> file and run it by
        clicking the green run icon in VS Code.</div>
    </li>
  </ol>
  <h3 id="testing">Testing Procedure</h3>
  <p>Verify that your test program works correctly by following each
    step in this procedure:</p>
  <ol class="test">
    <li>
      <div>Run your test program and ensure that your test
        program’s output is similar to the sample run output
        below.
        <pre class="console">&gt; python test_words.py
=================== test session starts ====================
platform win32--Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy
rootdir: C:\Users\cse111\week03
collected 2 items
test_words.py::test_prefix <span class="pass">PASSED                     [ 50%]</span>
test_words.py::test_suffix <span class="pass">PASSED                     [100%]</span>
<span class="pass">==================== 2 passed in 0.09s =====================</span></pre>
      </div>
    </li>
  </ol>
  <h3 id="solution">Sample Solution</h3>
  <p>When your program is finished, view the <a class="solution" href="https://byui-cse.github.io/cse111-ww-course/week03/samples/check_solution.html">sample solution</a> for this assignment to
    compare your solution to that one. Before looking at the sample
    solution, you should work to complete this checkpoint program.
    However, if you have worked on it for at least an hour and are still
    having problems, feel free to use the sample solution to help you
    finish your program.</p>
  <h4 id="call_graph">Call Graph</h4>
  <p>The following call graph shows the function calls and returns in
    the sample solution for this assignment. From this call graph we see
    that the computer starts executing the sample test functions by
    calling the <code>pytest.main</code> function. While executing the
    <code>pytest.main</code> function, the computer calls the
    <code>test_prefix</code> function. While executing the
    <code>test_prefix</code> function, the computer calls the
    <code>prefix</code> function. Then while still executing the
    <code>pytest.main</code> function, the computer calls the
    <code>test_suffix</code> function. While executing the
    <code>test_suffix</code> function, the computer calls the
    <code>suffix</code> function.
  </p>
  <figure class="center callgraph" style="width:31em">
    <img src="./test_password_files/call_graph_check.svg" alt="A function call graph for this assignment" title="A function call graph for this assignment">
  </figure>
  <h3 id="ponder">Ponder</h3>
  <p>During this assignment, you downloaded a Python file that
    contains two program functions named <code>prefix</code> and
    <code>suffix</code>. You wrote a test function named
    <code>test_suffix</code> that is similar to the
    <code>test_prefix</code> function that was given to you. You used
    <code>pytest</code> to run both test functions and examined the
    output of <code>pytest</code> to verify that the test functions
    passed. Because the test functions called <code>prefix</code> and
    <code>suffix</code> with many different arguments and verified
    (using <code>assert</code>) that the values returned from
    <code>prefix</code> and <code>suffix</code> were correct, we can
    assume that the <code>prefix</code> and <code>suffix</code>
    functions work correctly. Do you think writing and running test
    functions will help you write better programs?
  </p>
    <h3>Useful Links:</h3>
    <ul>
      <li>Return to: <a href="https://byui-cse.github.io/cse111-ww-course/week03/index.html">Week Overview</a> | <a href="https://byui-cse.github.io/cse111-ww-course/index.html">Course Home</a></li>
    </ul>
  </main>
  <footer>
    <p>Copyright © Brigham Young University-Idaho | All rights reserved</p>
  </footer>
  <script src="./test_password_files/highlight.min.js.download"></script>
  <script src="./test_password_files/highlightjs-line-numbers.min.js.download"></script>
  <script>
    hljs.highlightAll();
    hljs.initLineNumbersOnLoad();
  </script>


</body></html>