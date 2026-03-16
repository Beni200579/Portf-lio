import os
import urllib.parse
import re

pr_dir = r"c:\Users\Ebenezer Felismino\Desktop\portofolio\pr"
files = os.listdir(pr_dir)

# Sort files alphabetically
files.sort()

html_content = ""

for f in files:
    ext = os.path.splitext(f)[1].lower()
    # urlencode filename for src
    src = "pr/" + urllib.parse.quote(f)
    
    # Generate a readable title from filename
    title = f.replace(".png", "").replace(".mp4", "")
    if title.startswith("Captura de Tela ("):
        try:
            num = re.search(r'\d+', title).group(0)
            title_display = f"Projeto {num}"
        except:
            title_display = title
        desc = "Visualização estática da interface do projeto demonstrando o design system e a responsividade."
        tags = ['UI/UX', 'Design']
        tag_label = "Design Estático"
    elif title.startswith("Captura de tela "):
        time_str = title.replace("Captura de tela ", "")
        title_display = f"Interface {time_str}"
        desc = "Captura de tela detalhando os componentes do projeto num contexto de uso real."
        tags = ['Interface', 'Front-end']
        tag_label = "Visualização"
    elif title.startswith("Gravando "):
        time_str = title.replace("Gravando ", "")
        title_display = f"Demonstração {time_str}"
        desc = "Gravação de tela demonstrando o fluxo de interação, animações e a experiência de usuário."
        tags = ['Interação', 'Fluxo']
        tag_label = "Vídeo"
    else:
        title_display = title
        desc = "Detalhes do projeto em execução."
        tags = ['Projeto']
        tag_label = "Mídia"

    media_html = ""
    if ext == '.mp4':
        media_html = f'''                <div class="aspect-video overflow-hidden bg-slate-900 border-b border-white/5">
                    <video autoplay loop muted playsinline class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                        <source src="{src}" type="video/mp4">
                    </video>
                </div>'''
    elif ext in ['.png', '.jpg', '.jpeg']:
        media_html = f'''                <div class="aspect-video overflow-hidden border-b border-white/5">
                    <img src="{src}"
                        alt="{title_display}"
                        class="w-full h-full object-cover object-top transition-transform duration-700 group-hover:scale-105" />
                </div>'''
    else:
        continue

    tags_html = "\n                        ".join([f'<span class="px-3 py-1 rounded bg-white/5 text-xs text-slate-300 border border-white/5">{t}</span>' for t in tags])

    card_html = f'''            <article class="glass-card rounded-3xl overflow-hidden group">
{media_html}
                <div class="p-8">
                    <div class="text-brand-400 text-xs font-bold tracking-widest uppercase mb-3">{tag_label}</div>
                    <h3 class="text-2xl font-bold mb-3">{title_display}</h3>
                    <p class="text-slate-400 mb-6 line-clamp-3">{desc}</p>
                    <div class="flex gap-3">
                        {tags_html}
                    </div>
                </div>
            </article>\n'''
    
    html_content += card_html

with open(r"c:\Users\Ebenezer Felismino\Desktop\portofolio\new_grid.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated HTML successfully.")
