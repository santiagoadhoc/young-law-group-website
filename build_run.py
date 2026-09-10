# -*- coding: utf-8 -*-
"""Generates every page. Run: python build_run.py"""
from build import (write, pa_cards, PA, PA_HERO, pa_icon, BLOG, CDN, CDN2,
                   office_block, contact_form_section, redband_cta)
from blog_content import POST_BODY
from pa_content import PA_BODY

# ---------------- HOME nav/footer link fix is handled by regenerating index below? No: index.html kept as-is. ----------------

# ---------------- MEET THE TEAM ----------------
TEAM = [
 ("eric-young","Eric Young","Founder & Managing Partner",CDN2+"6793c5958afecba75ac0f93f_photo_2025-01-24_12-51-05%20(1).jpg"),
 ("laura-krieg","Laura Krieg","Advanced Certified Paralegal",CDN2+"67c5b65975d2313a09645ad4_LRK%20PHOTO%20copia.jpg"),
 ("gina-reed-miller","Gina Reed Miller","Client Care Coordinator",CDN2+"685953222a002fab7a87a24f_GetAttachmentThumbnail%20copia.jpg"),
]
DOGS = [
 ("Dash","Human &amp; Dog Resource Manager",CDN2+"67bdd467499e555f7362bbcd_6798014714d4a55965a81f74_Dash%2520Portrait%2520copia.jpeg"),
 ("Buster","Head of Security",CDN2+"67bdd46704ad80f5f68af171_67980139465f5442161105ff_20230509_003738%2520copia.jpeg"),
 ("Loki","Mischief Manager",CDN2+"67bdd4671fddfc8603a0b1c2_6798015ef3f20a8d6958fbc0_20240112_072624%2520copia.jpeg"),
 ("Rootbeer (Rootie)","Marketing Intern",CDN2+"67bdd46704a36e52a8bf299d_6797fc5f7de9b07827aeb751_Logo_(2)-transformed.jpeg"),
 ("Collin McDougall","",CDN2+"67bdd4679a6bb55035a2acb8_679946dc7f2f9d7f5c06e42d_P1010077%2520copia.jpeg"),
]
def team_cards(items, prefix=""):
    out='<div class="team-grid">'
    for slug,name,role,img in items:
        link_open = f'<a class="team-card reveal" href="{prefix}team/{slug}.html">' if slug else '<article class="team-card reveal">'
        link_close = '</a>' if slug else '</article>'
        out+=f'{link_open}<div class="team-photo"><img src="{img}" alt="{name}"></div><p class="team-role">{role}</p><h3 class="team-name">{name}</h3>{link_close}'
    out+='</div>'
    return out
def dog_cards(items):
    out='<div class="team-grid">'
    for name,role,img in items:
        role_html = f'<p class="team-role">{role}</p>' if role else ''
        out+=f'<article class="team-card reveal"><div class="team-photo"><img src="{img}" alt="{name}"></div>{role_html}<h3 class="team-name">{name}</h3></article>'
    out+='</div>'
    return out

VALUES = [
 ("Passionate","Passion drives everything we do at Young Law Group. We are deeply committed to standing by our clients during their most challenging times, providing unwavering support and compassionate guidance. Our passion fuels our determination to fight for justice and to help our clients rebuild their lives with dignity and confidence."),
 ("Skilled","We believe skill is essential to navigating the complexities of the legal system. Our team combines in-depth knowledge with sharp analytical abilities to craft effective strategies tailored to each client's unique needs. From thorough case preparation to persuasive courtroom advocacy, our skill ensures every case is handled with precision and care."),
 ("Experienced","Experience matters when seeking justice. With years of practice focused on personal injury cases, we've developed a deep understanding of the legal challenges our clients face. From complex litigation to compassionate client care, our experience allows us to anticipate obstacles, deliver solutions, and achieve the best possible outcomes."),
]
def values_block():
    out='<div class="values">'
    for i,(t,d) in enumerate(VALUES,1):
        out+=f'<div class="value-item reveal"><div class="num">{i}.</div><h3>{t}</h3><p>{d}</p></div>'
    out+='</div>'
    return out

meet_main = f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{CDN}679806a581f7787e3d7073c7_Roman%20Forum%20copia%20(1).jpg" alt="Classical architecture"></div>
  <div class="inner-hero-copy">
    <span class="eyebrow reveal">Meet The Team</span>
    <h1 class="reveal">Passionate. Skilled. Experienced.</h1>
    <p class="reveal">Trusted legal support when it matters most. At Young Law, we stand with those who have suffered serious, life-altering injuries. Our team is dedicated to securing the compensation and support you need to rebuild your life.</p>
  </div>
</section>
<section class="core section-grey"><div class="container">
  <div class="core-inner reveal">
    <h2 class="core-title">Skilled, Passionate, and Experienced: The Core of Young Law Group</h2>
    <p>We bring skill, passion, and experience to every case we handle. We truly take the time to understand your unique situation, address your concerns, and work tirelessly to achieve the justice you deserve. If you or a loved one has suffered a catastrophic injury, contact us today for a free consultation.</p>
    <a href="contact-us.html" class="btn btn-red">Contact Us For A Free Consultation</a>
  </div>
</div></section>
<section class="section"><div class="container">
  <h2 class="subhead center reveal">Meet our team</h2>
  <p class="section-sub center reveal" style="margin-left:auto;margin-right:auto">Experienced Personal Injury Attorneys Dedicated to Your Legal Needs</p>
  {team_cards(TEAM)}
  <h2 class="subhead center reveal" style="margin-bottom:34px">Meet our dog team</h2>
  {dog_cards(DOGS)}
</div></section>
<section class="section section-grey"><div class="container">
  <h2 class="subhead center reveal">Founding Principles &amp; Values</h2>
  {values_block()}
</div></section>
{office_block()}
"""
write("meet-the-team.html","Meet The Team - Young Law Group","Meet the experienced personal injury team at Young Law Group.",meet_main)

# ---------------- TEAM BIOS ----------------
BIOS = {
"eric-young":"""
<h2>Professional Experience</h2>
<p>Eric G. Young has represented seriously injured individuals since 1997.</p>
<p>With prior experience advocating for both plaintiffs and defendants, he brings a unique perspective to personal injury cases, understanding how to strategically and effectively represent his clients.</p>
<p>Over the years, Mr. Young has developed a strong background in civil litigation, trials, and appeals.</p>
<p>Notable successes include:</p>
<p><strong>Delgado v. Trax Bar &amp; Grill (2005)</strong> &mdash; A landmark premises liability case argued before the California Supreme Court. The decision established that business owners have a duty to protect patrons from harm, including assaults by others, and remains the leading precedent for cases of this type.</p>
<p><strong>Mata v. Mata (2003)</strong> &mdash; A premises liability appeal where the court held a bar responsible for negligent security that allowed an assailant to re-enter after being banned.</p>
<p>Mr. Young's experience in premises liability and personal injury law led to his selection by Thomson Reuters to author an article for the Causes of Action series: <em>"Cause of Action Against Tavern Owners, Restaurants, and Similar Businesses for Injuries Caused to Patrons by the Criminal Acts of Others."</em> This publication provides a state-by-state summary of third-party premises liability law and has been cited nationwide.</p>

<h2>Teaching and Academic Contributions</h2>
<p>Since 1999, Mr. Young has taught paralegal and law courses at the following institutions:</p>
<ul>
<li>Center for Advanced Legal Studies (CALS) &mdash; Houston, TX</li>
<li>Empire College &mdash; Santa Rosa, CA</li>
<li>Santa Rosa Junior College &mdash; Santa Rosa, CA</li>
<li>Sonoma State University &mdash; Rohnert Park, CA</li>
<li>Golden Gate University School of Law &mdash; San Francisco, CA</li>
<li>John F. Kennedy School of Law &mdash; Pleasant Hill, CA</li>
</ul>

<h2>Education and Memberships</h2>
<h3>Education</h3>
<ul>
<li>B.A. in Ancient &amp; Medieval History &mdash; University of Illinois, Urbana-Champaign</li>
<li>J.D. &mdash; Golden Gate University School of Law</li>
</ul>
<h3>Bar Admission</h3>
<p>Member in good standing, California State Bar</p>
<h3>Professional Memberships</h3>
<ul>
<li><strong>American Bar Association (ABA):</strong> Premier voluntary bar association for education and advocacy.</li>
<li><strong>American Association for Justice (AAJ):</strong> Focused on preserving justice and the right to trial by jury.</li>
<li><strong>California Lawyers Association (CLA):</strong> Oversees California's continuing legal education initiatives.</li>
<li><strong>Consumer Attorneys of California:</strong> Represents plaintiffs' lawyers and their clients.</li>
<li><strong>San Francisco Trial Lawyers Association (SFTLA):</strong> Promotes education and advocacy for Bay Area plaintiffs' attorneys.</li>
<li><strong>Association of Certified E-Discovery Specialists (ACEDS):</strong> Provides training in electronic discovery and evidence.</li>
<li><strong>California Advocates for Nursing Home Reform (CANHR):</strong> Advocates for quality care and long-term care consumer rights.</li>
<li><strong>Brain Injury Association of America (BIAA):</strong> Dedicated to improving the lives of individuals and families affected by brain injury.</li>
</ul>

<h2>Publications and Speaking Engagements</h2>
<p>Mr. Young frequently writes and speaks on legal technology and e-discovery topics.</p>
<ul>
<li>Author of <em>"Legal Tech-nicalities"</em>, a quarterly column for the Sonoma County Bar Association's Bar Journal.</li>
<li>Guest contributor for the One Legal Blog, the nation's leading provider of court electronic filing services.</li>
<li>Blogger at The Cyber-Esq., where he discusses developments in legal technology and practice management.</li>
</ul>

<h2>Personal Interests and Advocacy</h2>
<p>Outside the courtroom, Mr. Young enjoys reading and writing historical fiction and nonfiction, gardening, and digital photography.</p>
<p>He is deeply committed to animal welfare, wildlife conservation, and environmental justice &mdash; values reflected in Young Law Group's pro bono advocacy and financial support for related organizations.</p>
<p>Mr. Young lives with his spouse and their five rescue dogs &mdash; Buster, Dash, Loki, Gucci, and Root Beer &mdash; whose stories inspire the firm's ongoing commitment to animal rescue and protection.</p>
""",
"laura-krieg":"""
<h2>Professional Experience</h2>
<p>Laura R. Krieg, ACP, is an advanced certified paralegal with extensive experience in criminal law, personal injury, lien reduction, and family law. Since 2011, she has operated as a contract paralegal through her own firm, providing tailored legal support to clients across Sonoma County and beyond.</p>
<p>Her career includes over a decade of teaching paralegal and legal courses as an instructor in the Legal Department at Empire College, where she also served as the Head of the Legal Department from 2019 to 2021. During her tenure, Laura mentored aspiring legal professionals, sharing her experience in legal research, case management, and law office operations.</p>
<p>Before launching her independent paralegal services, Laura worked as a paralegal and office manager at Northern California Legal Group, where she supported attorneys in various practice areas, including immigration, civil litigation, and criminal defense.</p>

<h2>Education</h2>
<p>Sonoma State University, Rohnert Park, CA<br>Certificate in Paralegal Studies (2003&ndash;2005)</p>

<h2>Practice Areas</h2>
<ul>
<li>Criminal Law</li>
<li>Personal Injury</li>
<li>Lien Reduction</li>
<li>Family Law</li>
</ul>

<h2>Professional Associations and Certifications</h2>
<ul>
<li>Advanced Certified Paralegal (ACP)</li>
<li>Experience validated by peers and attorneys in legal research and technology, including Lexis.</li>
</ul>

<h2>Personal Interests and Advocacy</h2>
<p>Outside of her professional endeavors, Laura is passionate about education and mentoring the next generation of paralegals. She also enjoys spending time with her family, teaching dance, and advocating for animal rescue efforts.</p>
""",
"gina-reed-miller":"""
<h2>Professional Experience</h2>
<p>Gina brings over 40 years of healthcare experience, including nearly 30 years as a registered nurse. Beginning her career in the medical field, she steadily advanced, combining clinical knowledge with leadership and program development experience. Throughout her career, she has earned nationwide recognition for her contributions to cardiology, including helping establish standards of care and writing protocols for the American Heart Association (AHA).</p>
<p>Gina is known for her "I know I can" attitude and consistently excels in leadership roles. She leads by example, fosters collaboration, and is committed to delivering results that go above and beyond expectations. Her deep sense of responsibility, paired with her strong work ethic, has made her a trusted voice in healthcare.</p>

<h2>Leadership and Service</h2>
<p>From a young age, Gina has been actively involved in community and professional organizations, a commitment she has carried into adulthood. Her consistent involvement reflects her belief in service, contribution, and lifelong learning. She has been instrumental in mentoring peers and shaping best practices in patient care environments.</p>

<h2>Client Commitment</h2>
<p>Gina believes in truly listening to clients and advocates fiercely on their behalf. Her approach is rooted in empathy, experience, and a desire to ensure every individual feels heard, respected, and cared for. She is passionate about being a supportive first point of contact and takes pride in guiding people with compassion and clarity.</p>

<h2>Personal Background and Values</h2>
<p>Born and raised in the Midwest, Gina holds deep pride in her heritage and upbringing. Her values &mdash; honesty, hard work, and forward-thinking &mdash; continue to shape her professional approach. She is always looking ahead to anticipate what is needed and strives to deliver more than expected in every interaction.</p>
""",
}
LINKEDIN = {
    "eric-young": "https://www.linkedin.com/in/ericgyoung/",
    "laura-krieg": "https://www.linkedin.com/in/laura-r-krieg-acp-ab2b079/",
    # gina-reed-miller: no LinkedIn
}
pa_links_html = "".join(
    f'<li><a href="../practice-area/{s}.html">{t}</a></li>'
    for s,t,d,b in sorted(PA, key=lambda x: x[1])
)
for slug,name,role,img in TEAM:
    linkedin_link = f'<a href="{LINKEDIN[slug]}" target="_blank" rel="noopener">LinkedIn Profile</a>' if slug in LINKEDIN else ''
    main=f"""
<section class="section"><div class="container">
  <div class="bio reveal">
    <div class="bio-photo"><img src="{img}" alt="{name}">
      <div class="bio-meta">{linkedin_link}<a href="tel:+17073430556">(707) 343-0556</a></div>
    </div>
    <div class="bio-body">
      <h1>{name}</h1><div class="role">{role}</div>
      {BIOS[slug]}
      <a href="../contact-us.html" class="btn btn-red" style="margin-top:20px">Contact Us For A Free Consultation</a>
    </div>
  </div>
</div></section>
<section class="section section-grey pa-links-section"><div class="container">
  <h2 class="pa-links-title reveal">Practice Areas</h2>
  <ul class="pa-links reveal">{pa_links_html}</ul>
</div></section>
"""
    write(f"team/{slug}.html",f"{name} - Young Law Group",f"{name}, {role} at Young Law Group.",main)

# ---------------- PRACTICE AREAS (listing) ----------------
pa_main=f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{CDN}67980745929c380f4fae9eae_Pyramid%20to%20the%20Sky%202010%20copia.jpg" alt="Architecture"></div>
  <div class="inner-hero-copy">
    <span class="eyebrow reveal">Our Practice Areas</span>
    <h1 class="reveal">Advocating for Justice in Catastrophic Injury Cases</h1>
    <p class="reveal">Every case is unique, and we're here to provide the advocacy you deserve. Explore our practice areas to learn how we can help with catastrophic injury claims, serious accidents, and other complex legal matters.</p>
  </div>
</section>
<section class="section"><div class="container">{pa_cards()}</div></section>
{redband_cta()}
{office_block()}
"""
write("practice-areas.html","Practice Areas - Young Law Group","Explore the personal injury practice areas handled by Young Law Group.",pa_main)

# ---------------- PRACTICE AREA DETAIL ----------------
for slug,title,desc,body in PA:
    main=f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{PA_HERO}" alt="{title}"></div>
  <div class="inner-hero-copy">
    {pa_icon(slug, "margin-bottom:22px")}
    <h1 class="reveal">{title}</h1>
    <p class="reveal">{desc}</p>
    <a href="../contact-us.html" class="btn btn-red reveal">Free Consultation</a>
  </div>
</section>
<section class="section"><div class="container narrow">
  <p class="pa-intro reveal">{body}</p>
  <div class="article-body pa-article">{PA_BODY[slug]}</div>
</div></section>
{contact_form_section(CDN+"679808649f9032bbd507d972_lighthouse%20at%20point%20reyes%20national%20seashore,%20taken%20from%20above%20approach%20copia2.jpg")}
{office_block()}
"""
    write(f"practice-area/{slug}.html",f"{title} - Young Law Group",desc,main)

# ---------------- RESOURCES (blog listing) ----------------
def blog_card(slug, prefix=""):
    title,img,cat,rt,excerpt=BLOG[slug]
    return f"""<article class="insight-card reveal">
  <a href="{prefix}post/{slug}.html" class="insight-media"><img src="{img}" alt=""></a>
  <span class="insight-date">January 27, 2025</span>
  <div class="insight-foot"><h3><a href="{prefix}post/{slug}.html">{title}</a></h3>
  <a href="{prefix}post/{slug}.html" class="insight-arrow" aria-label="Read more">&rsaquo;</a></div>
</article>"""
news=[s for s in BLOG if BLOG[s][2]=="news"]
qa=[s for s in BLOG if BLOG[s][2]=="qa"]
res_main=f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{CDN}67994c4da81f96c1ee8964ef_Inside%20Hot%20Air%20Balloon%20copia.jpg" alt="Resources"></div>
  <div class="inner-hero-copy">
    <span class="eyebrow reveal">Resources</span>
    <h1 class="reveal">Helpful Guides, Insights, and Legal Resources</h1>
    <p class="reveal">Knowledge is power, especially when facing legal challenges. Our resource hub provides valuable information on personal injury law, your rights, and what to expect throughout the legal process.</p>
  </div>
</section>
<section class="section"><div class="container">
  <p class="blog-cat reveal">Legal News</p>
  <div class="blog-grid">{''.join(blog_card(s) for s in news)}</div>
  <p class="blog-cat reveal">Q&amp;A with Attorneys</p>
  <div class="blog-grid">{''.join(blog_card(s) for s in qa)}</div>
</div></section>
"""
write("resources.html","Resources - Young Law Group","Legal guides, insights, and resources from Young Law Group.",res_main)

# ---------------- BLOG POSTS ----------------
DISCOVER_RING = '''<div class="discover discover-sm" aria-hidden="true">
      <svg class="discover-ring" viewBox="0 0 200 200"><defs><path id="circlePathPost" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"></path></defs><text><textPath href="#circlePathPost">Discover more &nbsp;&bull;&nbsp; Discover more &nbsp;&bull;&nbsp; Discover more &nbsp;&bull;&nbsp;</textPath></text></svg>
      <span class="discover-chevron"></span>
    </div>'''
BLOG_SLUGS = list(BLOG)
BLOG_CATS = [("All Articles", True), ("Legal news", False), ("Q&amp;A with Attorneys", False), ("Client Success Stories", False)]
def related_row(slug):
    t,i,c,rt,ex = BLOG[slug]
    return f'''<div class="rel-post reveal">
      <div class="rel-post-text"><a href="{slug}.html" class="rel-post-title">{t}</a>
      <div class="post-meta">January 27, 2025 <span>&ndash;</span> {rt} min reading</div></div>
      <a href="{slug}.html" class="rel-read">Read<br>now</a>
    </div>'''
def category_nav():
    items = "".join(
        f'<li class="{ "active" if active else "" }">{name}</li>' for name, active in BLOG_CATS)
    return f'<ul class="cat-nav">{items}</ul>'

for idx, slug in enumerate(BLOG_SLUGS):
    title,img,cat,rt,excerpt = BLOG[slug]
    related = [BLOG_SLUGS[(idx+1) % len(BLOG_SLUGS)], BLOG_SLUGS[(idx+2) % len(BLOG_SLUGS)]]
    main=f"""
<section class="post-hero">
  <div class="reveal"><img class="image-cover" src="{img}" alt=""></div>
  <div class="post-hero-copy">
    <h1 class="reveal">{title}</h1>
    <div class="post-meta reveal">January 27, 2025 <span>&ndash;</span> {rt} min reading</div>
    {DISCOVER_RING}
  </div>
</section>
<section class="post-excerpt"><div class="container"><p class="reveal">{excerpt}</p></div></section>
<section class="section"><div class="container article">
  <h2 class="article-title reveal">{title}</h2>
  <div class="article-body pa-article">{POST_BODY[slug]}</div>
</div></section>
<section class="section section-grey more-articles"><div class="container">
  <div class="more-grid">
    <div class="more-list">
      <h2 class="reveal" style="margin-bottom:36px">More Articles</h2>
      {''.join(related_row(s) for s in related)}
    </div>
    {category_nav()}
  </div>
</div></section>
"""
    write(f"post/{slug}.html",f"{title} - Young Law Group",excerpt[:155],main)

# ---------------- COMMUNITY ----------------
CHARITIES=[
 ("International Fund for Animal Welfare (IFAW)",CDN+"67acb4cbb063f596963e2ec9_Ifaw_logo%20copia.png","The International Fund for Animal Welfare (IFAW) works globally to rescue and protect animals in need, employing innovative methods such as drone technology for wildlife conservation and anti-poaching initiatives. Founded in 1969, IFAW is committed to creating a world where animals and humans can coexist harmoniously. With over 90% of their funds allocated directly to impactful programs, they are a leader in animal rescue and advocacy."),
 ("Best Friends Animal Society",CDN+"67acb542743a44ae9426d1a3_7166584-logo%20copia.png","Best Friends Animal Society is dedicated to ending the killing of pets in shelters across the United States through groundbreaking no-kill initiatives. Their programs focus on spay/neuter efforts, adoption drives, and building a national network of no-kill shelters. Recognized for their financial accountability, they allocate approximately 88% of their funds to life-saving programs."),
 ("The Orangutan Project",CDN+"67acb58ad1a6a8c3d84597b3_top-logo-orange-360x263-1%20copia.png","The Orangutan Project is a leader in the fight to protect endangered orangutans and their habitats in Southeast Asia. Combining innovative conservation strategies with on-the-ground rescue and rehabilitation, the organization safeguards these incredible creatures. With over 90% of their funds directly supporting programs, they are a trusted advocate for wildlife conservation."),
]
CHARITY_URL = {
 "International Fund for Animal Welfare (IFAW)": "https://www.ifaw.org/",
 "Best Friends Animal Society": "https://bestfriends.org/",
 "The Orangutan Project": "https://www.theorangutanproject.org/",
}
def charity_logos():
    imgs = "".join(f'<img src="{img}" alt="{name}">' for name,img,desc in CHARITIES)
    return f'<section class="community-logos"><div class="container">{imgs}</div></section>'
def charity_list():
    out='<ul class="charity-list">'
    for name,img,desc in CHARITIES:
        url = CHARITY_URL.get(name, "#")
        out+=f'<li><strong>{name}</strong><br>{desc}<br><a href="{url}" target="_blank" rel="noopener">Visit their page.</a></li>'
    out+='</ul>'
    return out
comm_main=f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{CDN}67933a2d0991c8a9d761b171_Screenshot%202025-01-24%20at%202.57.55%20pm%20Large.jpeg" alt="Community"></div>
  <div class="inner-hero-copy">
    <span class="eyebrow reveal">Community Involvement</span>
    <h1 class="reveal">Giving Back to Our Community and Beyond</h1>
    <p class="reveal">At Young Law Group, we are dedicated to creating meaningful change &mdash; not just for our clients, but for the world around us. From the beginning, we pledged to support charitable organizations that share our values in animal welfare, environmental protection, and conservation.</p>
  </div>
</section>
{charity_logos()}
<section class="section"><div class="container narrow">
  <h2 class="community-title reveal">Pawsitive Giving Program</h2>
  <p class="reveal">At Young Law Group, we deeply value the responsibility of protecting those who cannot speak for themselves. That's why we proudly support organizations dedicated to advancing animal rights and welfare. These charities tirelessly combat cruelty, promote responsible pet ownership, and advocate for the dignity and well-being of all living creatures.</p>
  <blockquote class="community-quote reveal">&ldquo;The greatness of a nation and its moral progress can be judged by the way its animals are treated.&rdquo;<br>- Mahatma Gandhi</blockquote>
  {charity_list()}
  <h2 class="community-subhead reveal">Join Us in Creating Change</h2>
  <p class="reveal">We invite you to be part of our mission to support vital causes that advance animal welfare, protect the environment, and promote compassion. By working together, we can make a lasting impact, creating a future where all living beings thrive and our planet flourishes. Contact us to learn how you can get involved or contribute &mdash; together, we can shape a better world.</p>
  <blockquote class="community-quote reveal">&ldquo;It is our collective and individual responsibility to protect and nurture the global family, to support its weaker members and to preserve and tend to the environment in which we all live.&rdquo; -Dalai Lama</blockquote>
</div></section>
"""
write("community.html","Community Involvement - Young Law Group","Young Law Group's community involvement and charitable giving.",comm_main)

# ---------------- REPRESENTATIVE CASES ----------------
CASES=[
 ("$65,000","Fight at Fast Food Restaurant","Client assaulted by an employee of a fast food restaurant and sustained minor injuries, with no wage loss."),
 ("$275,000","Assisted Living Facility Negligence","Client fell and sustained a head laceration at an assisted living facility. Settlement obtained shortly after the complaint was served and before discovery commenced."),
 ("$200,000","Trip and Fall at Grocery Store","Client tripped over a parking bumper in front of a grocery store, sustaining injury."),
 ("$65,000","Sideswipe Automobile Collision Causing Minor Injuries","Client suffered soft tissue back injuries."),
 ("$150,000","Rear End Collision Causes Multi-Car Accident","Client was injured when a vehicle in the opposite lane of traffic was struck from behind and pushed into the driver's side of the client's vehicle."),
]
def cases_block():
    out='<div class="cases-list">'
    for amt,title,desc in CASES:
        out+=f'<div class="case-item reveal"><span class="amt">{amt}</span><h3>{title}</h3><p>{desc}</p></div>'
    out+='</div>'
    return out
cases_main=f"""
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="{CDN}67be0fe550ef28ffa4438113_Point%20Reyes%20National%20Seashore%2C%20Northern%20California.JPG" alt="Northern California coast"></div>
  <div class="inner-hero-copy">
    <span class="eyebrow reveal">Representative Cases</span>
    <h1 class="reveal">Proven Results in the Pursuit of Justice</h1>
    <p class="reveal">At Young Law Group, we are committed to fighting for those who have endured serious injustices. With unwavering dedication, we work to secure the compensation and accountability our clients deserve.</p>
  </div>
</section>
<section class="section"><div class="container">
  <h2 class="subhead center reveal">Our firm gets results</h2>
  {cases_block()}
  <p class="center italic reveal" style="margin-top:30px;color:#777;font-size:14px;max-width:760px;margin-left:auto;margin-right:auto">Prior results do not guarantee a similar outcome. Every case is unique and results depend on the specific facts and circumstances.</p>
</div></section>
{office_block()}
"""
write("representative-cases.html","Representative Cases - Young Law Group","Representative case results from Young Law Group.",cases_main)

# ---------------- CONTACT US ----------------
contact_main=f"""
<section class="section contact-head"><div class="container">
  <div class="contact-head-grid">
    <div>
      <h1 class="contact-head-title reveal">Contact Us</h1>
      <p class="contact-head-sub reveal">Helping Clients Across California Achieve the Justice They Deserve</p>
    </div>
    <div class="discover discover-sm" aria-hidden="true">
      <svg class="discover-ring" viewBox="0 0 200 200"><defs><path id="circlePathContact" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"></path></defs><text><textPath href="#circlePathContact">Discover more &nbsp;&bull;&nbsp; Discover more &nbsp;&bull;&nbsp; Discover more &nbsp;&bull;&nbsp;</textPath></text></svg>
      <span class="discover-chevron"></span>
    </div>
  </div>
</div></section>
<section class="redband contact-cta"><div class="container">
  <div class="contact-cta-cols reveal">
    <p><strong>Your Case. Your Justice. Your Future.</strong><br>At Young Law Group, we provide personalized legal representation for those facing life-altering challenges. Whether you&rsquo;ve suffered a catastrophic injury, medical negligence, or elder abuse, our experienced team is here to guide you. Every case is unique, and we take the time to understand your situation and craft a strategy to secure the justice and compensation you deserve.</p>
    <p><strong>Free, No-Obligation Consultation</strong><br>Tell us your story, and let&rsquo;s start fighting for you today. Your initial consultation is completely free&mdash;and there&rsquo;s no time limit. We&rsquo;re here to help you explore your options, take control of your future, and seek the justice you deserve. Contact us today&mdash;let Young Law Group be your trusted partner in rebuilding your life.</p>
  </div>
</div></section>
{contact_form_section(CDN+"679808649f9032bbd507d972_lighthouse%20at%20point%20reyes%20national%20seashore,%20taken%20from%20above%20approach%20copia2.jpg")}
{office_block()}
"""
write("contact-us.html","Contact Us - Young Law Group","Contact Young Law Group for a free personal injury consultation.",contact_main)

# ---------------- EXISTING CLIENTS (password gate -> separate portal page) ----------------
ec_main="""
<section class="pw-wrap" id="pwGate">
  <h1>Existing Clients</h1>
  <p>This area is password protected. Please enter the password provided by our office to access your client resources.</p>
  <form class="pw-form" id="pwForm">
    <input type="password" placeholder="Password" aria-label="Password" id="pwInput" autocomplete="current-password">
    <button type="submit" class="btn btn-red btn-block">Enter</button>
    <p class="form-status" id="pwStatus" style="text-align:center"></p>
  </form>
</section>
<script>
(function(){
  var PW = "YoungLaw123*!";
  document.getElementById('pwForm').addEventListener('submit', function(e){
    e.preventDefault();
    if (document.getElementById('pwInput').value === PW) {
      try { sessionStorage.setItem('ylg_client_ok', '1'); } catch(err){}
      window.location.href = 'client-portal.html';
    } else {
      document.getElementById('pwStatus').textContent = 'Incorrect password. Please try again or contact our office.';
    }
  });
})();
</script>
"""
write("existing-clients.html","Existing Clients - Young Law Group","Existing client portal for Young Law Group.",ec_main)

# ---------------- CLIENT PORTAL (revealed after password) ----------------
portal_main="""
<script>
try { if (sessionStorage.getItem('ylg_client_ok') !== '1') { window.location.replace('existing-clients.html'); } } catch(err) { window.location.replace('existing-clients.html'); }
</script>
<section class="inner-hero">
  <div class="reveal"><img class="image-cover" src="/images/679806c943716d8c935d12bd_GG%20Bridge%20With%20Ship%20Underneath%20Original%20Output%20(1)%20copia%20(1).jpg" alt="San Francisco Bay and the Golden Gate Bridge"></div>
  <div class="inner-hero-copy">
    <h1 class="contact-head-title reveal">Client Portal</h1>
    <p class="contact-head-sub reveal">Everything you need to stay connected with our team</p>
    <p class="reveal" style="font-size:16.5px;margin-top:22px;max-width:560px">At Young Law Group, we believe strong relationships don&rsquo;t end once your case begins, they grow through clear communication and continued support. Our goal is to make it easy for you to stay informed, connected, and confident every step of the way. Through our Client Portal, 24/7 reception, and new client outreach initiatives, we&rsquo;re here to ensure your experience is seamless and personal from start to finish.</p>
  </div>
</section>
<section class="section"><div class="container narrow">
  <h2 class="community-title reveal">Clio Connect Portal</h2>
  <p class="reveal">Our secure Client Portal, powered by <strong>Clio Connect</strong>, gives you 24/7 access to your case information. You can view and download documents, track important updates, review invoices, and communicate directly with our team, all in one convenient location.</p>
  <p class="reveal"><a href="https://account.clio.com/" target="_blank" rel="noopener" class="link-underline">Login to the Client Portal</a></p>

  <h2 class="community-title reveal" style="margin-top:64px">24/7 Reception &amp; Text Line</h2>
  <p class="reveal">We understand that questions don&rsquo;t always come up during business hours. That&rsquo;s why we&rsquo;ve partnered with a <strong>24/7 reception service</strong> to ensure your calls are always answered. If you prefer to text, you can reach us anytime at <strong><a href="sms:+18336351741" style="color:inherit">833-635-1741</a></strong>.</p>
  <p class="reveal">Messages sent after hours will be routed to our team and answered as soon as possible the next business day.</p>

  <h2 class="community-title reveal" style="margin-top:64px">Stay Connected</h2>
  <p class="reveal">We&rsquo;re always finding new ways to keep our clients informed and engaged. From our upcoming <strong>firm newsletter</strong> and <strong>podcast</strong> to regular announcements and community updates, we look forward to sharing insights, stories, and news that matter to you.</p>
</div></section>
"""
write("client-portal.html","Client Portal - Young Law Group","Young Law Group client portal.",portal_main)

print("ALL PAGES BUILT")
