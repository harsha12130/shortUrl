URL Shortener – Django Project
------------------------------
A simple and efficient URL Shortener built using Django.
Users can submit long URLs and receive a short, shareable link that redirects to the original destination.

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Django URL Shortener — README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#95a0b8; --accent:#7dd3fc;
      --glass: rgba(255,255,255,0.03);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071126 0%,#071733 100%);color:#e6eef8}
    .container{max-width:900px;margin:48px auto;padding:28px;background:var(--card);border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,0.6);border:1px solid rgba(255,255,255,0.03)}
    header h1{margin:0;font-size:1.75rem;letter-spacing:-0.2px}
    header p{color:var(--muted);margin-top:6px}
    .section{margin-top:22px}
    .section h2{margin:0 0 8px 0;font-size:1.05rem;color:var(--accent)}
    .list{color:var(--muted);margin:8px 0 0 18px}
    .list li{margin:6px 0}
    .code{
      margin:14px 0;
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:8px;padding:14px;overflow:auto;border:1px solid rgba(255,255,255,0.03);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
      color:#dbeafe; font-size:0.95rem; line-height:1.5
    }
    .inline-code{background:rgba(255,255,255,0.03);padding:2px 6px;border-radius:6px;font-family:inherit}
    pre{margin:0}
    .meta{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px;color:var(--muted)}
    .badge{background:var(--glass);padding:6px 10px;border-radius:999px;border:1px solid rgba(255,255,255,0.02)}
    footer{margin-top:28px;color:var(--muted);font-size:0.9rem;text-align:center}
    a{color:var(--accent);text-decoration:none}
    a:hover{text-decoration:underline}
    /* simple syntax highlight - not exhaustive */
    .token-key{color:#7dd3fc}
    .token-str{color:#a7f3d0}
    .token-comment{color:#94a3b8;font-style:italic}
    @media (max-width:640px){.container{margin:18px;padding:18px}}
  </style>
</head>
<body>
  <div class="container" role="main">
    <header>
      <h1>Django URL Shortener</h1>
      <p>A simple and powerful URL shortening service built with Django 4.2.26 and Python 3.9.6.</p>
      <div class="meta">
        <span class="badge">Django 4.2.26</span>
        <span class="badge">Python 3.9.6</span>
        <span class="badge">SQLite (default)</span>
        <span class="badge">HTML / CSS / JS</span>
      </div>
    </header>

    <section class="section" id="features">
      <h2>🚀 Features</h2>
      <ul class="list">
        <li>Shorten any valid URL</li>
        <li>Automatic generation of unique short codes</li>
        <li>Redirect short links to original URLs</li>
        <li>Django-based MVC structure</li>
        <li>Stores URLs in SQLite (default Django DB)</li>
        <li>Clean and simple UI</li>
      </ul>
    </section>

    <section class="section" id="deployment">
      <h2>🌐 Deployment</h2>
      <p>Live demo: <a href="https://url.pythonanywhere.com/" target="_blank" rel="noopener">https://url.pythonanywhere.com/</a></p>
    </section>

    <section class="section" id="project-structure">
      <h2>📂 Project Structure</h2>
      <div class="code" role="region" aria-label="project structure">
<pre><code>url-shortener/
├── url/                # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shortener/          # App that handles URL shortening
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
├── db.sqlite3
├── manage.py
└── README.html
</code></pre>
      </div>
    </section>

    <section class="section" id="installation">
      <h2>⚙️ Installation & Setup</h2>
      <ol class="list">
        <li>Clone the repository:
          <div class="code"><pre><code>git clone https://github.com/&lt;your-user&gt;/url-shortener.git
cd url-shortener</code></pre></div>
        </li>
        <li>Create a virtual environment:
          <div class="code"><pre><code>python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows</code></pre></div>
        </li>
        <li>Install dependencies:
          <div class="code"><pre><code>pip install -r requirements.txt</code></pre></div>
        </li>
        <li>Apply migrations:
          <div class="code"><pre><code>python manage.py migrate</code></pre></div>
        </li>
        <li>Run the development server:
          <div class="code"><pre><code>python manage.py runserver
# Open http://127.0.0.1:8000/</code></pre></div>
        </li>
      </ol>
    </section>

    <section class="section" id="how-it-works">
      <h2>🧠 How It Works</h2>
      <ol class="list">
        <li>User submits a long URL via the UI.</li>
        <li>The app generates a short, unique code (e.g., <span class="inline-code">abc123</span>).</li>
        <li>The short link (<span class="inline-code">/abc123</span>) redirects to the original URL.</li>
      </ol>
    </section>

    <section class="section" id="example-model">
      <h2>📜 Example Model — <small>shortener/models.py</small></h2>
      <div class="code" aria-label="example model code">
<pre><code><span class="token-key">from</span> django.db <span class="token-key">import</span> models
<span class="token-key">import</span> string, random

<span class="token-key">class</span> URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    <span class="token-key">def</span> save(self, *args, **kwargs):
        <span class="token-key">if</span> <span class="token-key">not</span> self.short_code:
            self.short_code = ''.join(random.choice(string.ascii_letters) <span class="token-key">for</span> _ <span class="token-key">in</span> <span class="token-key">range</span>(6))
        super().save(*args, **kwargs)

    <span class="token-key">def</span> __str__(self):
        <span class="token-key">return</span> self.short_code
</code></pre>
      </div>
    </section>

    <section class="section" id="example-view">
      <h2>📜 Example View — <small>shortener/views.py</small></h2>
      <div class="code" aria-label="example view code">
<pre><code><span class="token-key">from</span> django.shortcuts <span class="token-key">import</span> render, redirect, get_object_or_404
<span class="token-key">from</span> .models <span class="token-key">import</span> URL

<span class="token-key">def</span> home(request):
    <span class="token-key">if</span> request.method == "POST":
        long_url = request.POST.get("long_url")
        url_obj = URL(long_url=long_url)
        url_obj.save()
        short = request.build_absolute_uri('/') + url_obj.short_code
        <span class="token-key">return</span> render(request, "index.html", {"short": short})
    <span class="token-key">return</span> render(request, "index.html")

<span class="token-key">def</span> redirect_short(request, short_code):
    obj = get_object_or_404(URL, short_code=short_code)
    <span class="token-key">return</span> redirect(obj.long_url)
</code></pre>
      </div>
    </section>

    <section class="section" id="notes">
      <h2>📝 Notes</h2>
      <ul class="list">
        <li>By default the project uses SQLite (file: <span class="inline-code">db.sqlite3</span>).</li>
        <li>Adjust <span class="inline-code">settings.py</span> to use PostgreSQL/MySQL if needed for production.</li>
        <li>Make sure to add allowed hosts and configure static files when deploying (PythonAnywhere, Heroku, etc.).</li>
      </ul>
    </section>

    <footer>
      <div>Made with ❤ — <strong>Konanki Harshavardhan</strong></div>
      <div style="margin-top:6px;color:var(--muted)">Project live at <a href="https://url.pythonanywhere.com/" target="_blank" rel="noopener">url.pythonanywhere.com</a></div>
    </footer>
  </div>
</body>
</html>



<img width="1437" height="531" alt="image" src="https://github.com/user-attachments/assets/bd1dc45f-32c4-4fb2-b410-5aa946b331c0" />
<img width="1437" height="542" alt="image" src="https://github.com/user-attachments/assets/839f912e-c203-4ca5-b776-d5f9b4676f1c" />
<img width="1440" height="560" alt="image" src="https://github.com/user-attachments/assets/f3da3ab0-15ef-462f-8835-2f45841a2b6a" />


