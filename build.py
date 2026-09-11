# -*- coding: utf-8 -*-
"""Static-site generator for Young Law Group. Rebuilds the client's own Webflow
site as consistent static HTML. Run: python build.py"""
import os, html

CDN = "/images/"
CDN2 = "/images/"
LOGO = CDN + "67bdd0f87988247ee898c0b7_Young%20law%20logo%20original%20letras%20negras%20copia.png"

NAV_LINKS = [
    ("Meet The Team", "meet-the-team.html"),
    ("Practice Areas", "practice-areas.html"),
    ("Resources", "resources.html"),
    ("Community", "community.html"),
    ("Cases", "representative-cases.html"),
]

def head(title, desc, p):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" type="image/png" href="/images/Icon.png">
<link rel="apple-touch-icon" href="/images/Icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Young Law Group">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://younglawca.com/images/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="https://younglawca.com/images/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/styles.css">
</head>
<body>"""

def nav(p):
    links = "".join(f'<a href="{p}{href}">{name}</a>' for name, href in NAV_LINKS)
    mlinks = "".join(f'<a href="{p}{href}">{name}</a>' for name, href in NAV_LINKS)
    return f"""
<header class="nav" id="nav">
  <div class="container nav-inner">
    <a href="{p}index.html" class="nav-logo" aria-label="Young Law Group home"><img src="{LOGO}" alt="Young Law Group"></a>
    <nav class="nav-links" aria-label="Primary">{links}</nav>
    <a href="{p}contact-us.html" class="btn btn-red nav-cta">Contact Us</a>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
  <div class="nav-mobile" id="navMobile">{mlinks}<a href="{p}contact-us.html" class="btn btn-red">Contact Us</a></div>
</header>
<main>"""

def footer(p):
    return f"""</main>
<footer class="footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img class="footer-logo" src="{LOGO}" alt="Young Law Group">
      <p>If you&rsquo;ve been injured due to negligence, contact Young Law Group today to schedule a consultation and learn how we can help you navigate the legal system and fight for the justice you deserve.</p>
    </div>
    <ul class="footer-col">
      <li><a href="{p}index.html">Home</a></li>
      <li><a href="{p}contact-us.html">Contact Us</a></li>
      <li><a href="{p}representative-cases.html">Representative Cases</a></li>
    </ul>
    <ul class="footer-col">
      <li><a href="{p}resources.html">Resources</a></li>
      <li><a href="{p}practice-areas.html">Practice Areas</a></li>
      <li><a href="{p}existing-clients.html">Existing Clients</a></li>
    </ul>
    <ul class="footer-col">
      <li><a href="{p}meet-the-team.html">Meet The Team</a></li>
      <li><a href="{p}community.html">Community Involvement</a></li>
    </ul>
  </div>
  <div class="footer-legal">
    <div class="container footer-legal-row">
      <span>&copy; 2025 All right reserved</span>
      <a href="#">Privacy Policy</a><a href="#">Terms of Use</a><a href="#">Anti-Spam</a>
    </div>
  </div>
</footer>
<script src="{p}js/main.js"></script>
<!-- Intaker chat / intake widget -->
<script>(function (w,d,s,v,odl){{(w[v]=w[v]||{{}})['odl']=odl;
var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;
j.src='https://intaker.azureedge.net/widget/chat.min.js';
f.parentNode.insertBefore(j,f);
}})(window, document, 'script','Intaker', 'younglaw');</script>
</body>
</html>"""

# Reusable office + contact-form blocks
def office_block():
    return """
<section class="office"><div class="container">
  <h2 class="reveal">Find Us in Your Area: <span class="red">Our Cotati Office</span></h2>
  <div class="office-grid reveal"><div class="office-block">
    <h4 class="red italic">Office Address</h4>
    <div class="office-row"><a href="tel:+17073430556">(707) 343-0556</a><span>315 East Cotati Avenue,<br>Cotati, California 94931.</span></div>
    <h4 class="red italic">Mailing Address</h4><p>PO Box 206, Cotati, California 94931.</p>
    <h4 class="red italic">Office Hours &amp; Availability</h4>
    <div class="office-hours"><div><strong>Monday &ndash; Thursday:</strong><span>8:30 AM &ndash; 5:00 PM</span></div><div><strong>Friday:</strong><span>Closed.</span></div></div>
    <p class="italic">Evening / Weekend appointments available on request.</p>
  </div></div>
</div></section>"""

def contact_form_section(img):
    return f"""
<section class="contact"><div class="contact-grid">
  <div class="contact-media reveal"><img class="image-cover" src="{img}" alt="California coast"></div>
  <form class="contact-form reveal" id="leadForm" action="#" method="post" novalidate>
    <label><span class="field-label">Full Name <span class="req">*</span></span><input type="text" name="full_name" required></label>
    <label><span class="field-label">Phone Number <span class="req">*</span></span><input type="tel" name="phone" required placeholder="(707) 000 0000"></label>
    <label><span class="field-label">Email <span class="req">*</span></span><input type="email" name="email" required></label>
    <label><span class="field-label">Message</span><textarea name="message" rows="3"></textarea></label>
    <button type="submit" class="btn btn-red btn-block">Submit</button>
    <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
  </form>
</div></section>"""

def redband_cta():
    return """
<section class="redband"><div class="container">
  <h2 class="reveal">Request a Free Consultation Today</h2>
  <div class="redband-cols">
    <p class="reveal">Young Law Group is dedicated to helping you navigate legal issues related to Personal Injury, Slip and Fall Accidents, Dangerous Conditions on Public or Private Property, Auto Accidents, Defective Products, Wrongful Death, Medical Negligence, and Elder or Nursing Home Abuse.</p>
    <p class="reveal">We&rsquo;re here to provide the answers and guidance you need during this difficult time. Contact us today to schedule your free, no-time-limit consultation and speak with an experienced attorney about your case. Let us help you take the first step toward justice and the compensation you deserve.</p>
  </div>
</div></section>"""

def write(path, title, desc, main_html):
    depth = path.count("/")
    p = "../" * depth
    full = head(title, desc, p) + nav(p) + main_html + footer(p)
    full_path = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full_path) or ".", exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(full)
    print("wrote", path)

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- PRACTICE AREAS DATA ----------
PA_HERO = CDN + "6780ccb820541ecf08c75355_pexels-brett-sayles-1000740_3_11zon.webp"
ICON = {
 "auto-accidents": CDN2+"67bdf4f9d1f805a31116e83a_6793d2cf3e67834320e90f90_car_5723686%20copia.png",
 "pedestrian-bicycle-accidents": CDN2+"67bdf72cd35b87dc9261ffea_6793d2385c76154821e032be_bicycle_10258618%20copia.png",
 "slip-trip": CDN2+"67bdf67d7acf006f4fd5b296_6793d19a1efde8cacfc3f075_slippery-floor_17732570%20copia.png",
 "dangerous-conditions-property": CDN2+"67bdf6ca7c18e54866a6ac5f_6793d1a6a92d634fbcbfd1de_warning-sign-icon_17732534%20copia.png",
 "defective-products": CDN2+"67bdf6f55e2cf438f7219299_6793d20a0a92f309ddc241cc_render_11773992%20copia.png",
 "elder-abuse-neglect": CDN2+"67bdf5d17622b0a239b3b623_6797f4f3c86a6612011d4358_disable%20copia.png",
 "nursing-home-abuse-neglect": CDN2+"67bdf6003364627ca8971701_6793de1090ef8edab791d7b6_hospital_6379635%20copia.png",
 "assault-battery": CDN2+"67bdf59c0481ea24bf7ce2d5_6793def01aada6e90b480eab_hand%20copia.png",
 "construction-site-injuries": CDN2+"67bdf764e78ff022d0916f21_6793d32863d185fe4eea3a95_crane%20copia.png",
 "other-personal-injuries-f5vlz": CDN2+"67bdf7a09619216587372b48_6793df1682601969f06a1e79_broken-arm_8011356%20copia.png",
 "wrongful-death-7ufzp": CDN2+"67d06c5b1f12be31ab82c5b9_tomb.png",
 "consumer-fraud": CDN2+"6839c41aaeb86d8cd8a81182_Eric%20Young%20-%20Image%20Assets.png",
}
# these two original icons come with the red circle baked in -> render as-is (no CSS circle, no filter)
FULL_ICON = {"wrongful-death-7ufzp", "consumer-fraud"}
SVG_TOMB = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 21V10a6 6 0 0 1 12 0v11z"/><line x1="4" y1="21" x2="20" y2="21"/><line x1="12" y1="8" x2="12" y2="14"/><line x1="9" y1="11" x2="15" y2="11"/></svg>'
SVG_FRAUD = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'

PA = [
 ("auto-accidents","Auto Accidents","Manage cases involving auto accidents, ranging from minor collisions to multi-vehicle crashes, often resulting in severe injuries or fatalities.","Auto accidents, from minor collisions to multi-vehicle pileups, can cause catastrophic injuries and fatalities. With over 38,000 fatalities annually on U.S. roadways, Young Law Group is committed to fighting for victims and ensuring they receive the compensation they deserve. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("pedestrian-bicycle-accidents","Pedestrian/Bicycle Accidents","Represent cases involving pedestrians, bicyclists, and motorized vehicles such as e-scooters, addressing the specific legal complexities involved.","Drivers are responsible for keeping roadways safe for pedestrians, bicyclists, and motorized scooter users. Young Law Group has the experience to navigate the unique legal challenges these cases present and advocate for injured victims. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("slip-trip","Slip/Trip and Fall Injuries","Assist with cases involving slip and fall or trip and fall accidents, including injuries ranging from sprains to traumatic brain injuries.","Slip and trip accidents caused by unforeseen hazards can lead to severe injuries, especially for older individuals. Common injuries include harm to the ankles, wrists, and arms, but in some cases, falls result in life-altering conditions like traumatic brain injuries. Young Law Group has extensive experience handling these cases and securing justice for victims. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("dangerous-conditions-property","Dangerous Conditions of Property","Handle cases involving injuries caused by dangerous conditions on public or private property, from hazardous materials to unsafe playgrounds.","Negligent property owners and poorly maintained public spaces can create hazardous conditions, such as dangerous chemicals, unmarked crosswalks, or broken traffic signals. These risks can result in a wide range of injuries. Young Law Group is experienced in holding property owners and municipalities accountable for their negligence. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("defective-products","Defective Products","Injuries caused by defective products, devices, or drugs often involve serious legal complexities and significant consequences.","Defective products, such as faulty medical devices or harmful drugs, can result in serious or fatal injuries. In these cases, manufacturers, designers, and distributors can be held liable. Young Law Group has deep experience with product liability claims to hold negligent parties accountable. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("wrongful-death-7ufzp","Wrongful Death","Pursue wrongful death cases involving emotional harm, loss of financial support, and other damages caused by negligence or misconduct.","When negligence or misconduct leads to the loss of a loved one, family members can file wrongful death lawsuits for compensation, including emotional and financial damages. Young Law Group has the experience needed to handle these complex cases with care and determination. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("elder-abuse-neglect","Elder Abuse/Neglect","Advocate for elders who have suffered abuse, neglect, or financial exploitation, leveraging California's strong elder protection laws to safeguard their rights.","Elder abuse, including physical harm, neglect, or financial exploitation, is a grave issue. California's strong elder protection laws allow Young Law Group to fight for justice for seniors who have been wronged. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("nursing-home-abuse-neglect","Nursing Home Abuse/Neglect","Represent victims of neglect or abuse in nursing homes and long-term care facilities, seeking justice for physical, mental, or emotional harm caused by inadequate care.","Elderly residents in nursing homes deserve proper care, but neglect and abuse are all too common. Young Law Group has successfully represented residents who have suffered due to inadequate attention or mistreatment in these facilities. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("consumer-fraud","Consumer Fraud","Pursue consumer fraud claims against businesses or individuals that engage in deceptive, misleading, or unfair practices, resulting in financial harm or loss to consumers.","Consumer fraud occurs when businesses or individuals use deceptive, misleading, or unfair tactics to take advantage of consumers. These cases often involve false advertising, hidden fees, or scams that result in financial loss. As a challenging area of law that demands attention to detail and aggressive advocacy, consumer fraud claims require skilled legal support. Contact Young Law Group today to schedule your free consultation and find out how we can help protect your rights."),
 ("assault-battery","Assault/Battery","Handle cases involving intentional misconduct, such as assault or battery, to secure compensation for physical harm, emotional distress, and punitive damages.","Assault involves fear of imminent harm, while battery includes actual physical contact. These intentional acts can result in significant compensation for victims, including punitive damages. Young Law Group is skilled at navigating these cases and addressing their unique challenges. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("construction-site-injuries","Construction Site Injuries","Advocate for construction workers injured by negligence, unsafe conditions, or inadequate safety precautions.","Construction sites are inherently dangerous, but negligence by contractors or insufficient safety measures can lead to severe injuries. Young Law Group aggressively represents injured workers to ensure their rights are protected. Contact Young Law Group today to schedule your free consultation and see how we can help."),
 ("other-personal-injuries-f5vlz","Other Personal Injuries","Address cases involving emotional, psychological, or reputational harm, as well as injuries caused by defamation, privacy violations, or consumer fraud.","Personal injuries are not always physical. Emotional, psychological, and reputational harm, such as defamation or privacy invasion, can have long-lasting effects. Young Law Group handles these cases with care, including those involving disability discrimination and workers' rights. Contact Young Law Group today to schedule your free consultation and see how we can help."),
]
def pa_icon(slug, style=""):
    cls = "pa-icon pa-icon-full" if slug in FULL_ICON else "pa-icon"
    st = f' style="{style}"' if style else ""
    return f'<span class="{cls}"{st}><img src="{ICON[slug]}" alt=""></span>'

def pa_cards(prefix=""):
    out='<div class="pa-grid">'
    for slug,title,desc,body in PA:
        out+=f'<a class="pa-card reveal" href="{prefix}practice-area/{slug}.html">{pa_icon(slug)}<h3>{title}</h3><p>{desc}</p></a>'
    out+='</div>'
    return out

# ---------- BLOG DATA ----------
# (title, image, category, reading_time_min, excerpt)
BLOG = {
 "top-legal-resources-for-northern-california-residents": ("Top Legal Resources for Northern California Residents", CDN2+"67980cf84480db781e1f1c92_2151325856.jpg", "news", "4", "Explore essential legal resources in Northern California, including referral services, advocacy groups, and legal aid organizations to help you navigate your legal needs with confidence. Whether you need guidance, representation, or support, these resources can provide valuable assistance. Request a free consultation today to discuss your case and take the first step toward the legal help you deserve."),
 "how-to-find-the-right-legal-representation-in-california": ("How to Find the Right Legal Representation in California", CDN2+"67980da54b33a60ce4ef3975_3749.jpg", "news", "4", "Learn practical tips for choosing the right attorney, from identifying your legal needs to checking credentials and scheduling consultations. Explore trusted resources and guidance to help you find skilled legal representation. Request a free consultation today and take the first step toward securing the legal support you need."),
 "legal-support-for-seniors-protecting-rights-and-preventing-abuse": ("Legal Support for Seniors: Protecting Rights and Preventing Abuse", CDN2+"67980f85bdb5da3135e38501_14500.jpg", "news", "3", "Discover essential legal resources and protections for seniors, including support for combating elder abuse, preventing financial exploitation, and estate planning. Learn how Young Law Group can help safeguard the rights and dignity of seniors. Request a free consultation today to discuss your needs and ensure your loved ones receive the protection they deserve."),
 "essential-resources-for-lgbtq-legal-and-community-support-in-northern-california": ("Essential Resources for LGBTQ Legal and Community Support in Northern California", CDN2+"6798105782c838efbf89e4b2_2148165403.jpg", "qa", "5", "Discover key resources for LGBTQ+ individuals, including legal advocacy, family support, youth programs, and healthcare services. Find the support you need to protect your rights and build a stronger community. Request a free consultation today to explore your legal options and ensure you have the protection and representation you deserve."),
 "navigating-legal-services-for-low-income-families-in-california": ("Navigating Legal Services for Low-Income Families in California", CDN2+"6798114972a9259ee7d606a6_13572.jpg", "qa", "6", "Discover essential resources and organizations offering free or low-cost legal aid for housing, public benefits, and family law. Learn how to access trusted guidance and support to protect your rights. Request a free consultation today to explore your options and get the legal help you need."),
 "animal-rights-and-welfare-key-legal-organizations-in-california": ("Animal Rights and Welfare: Key Legal Organizations in California", CDN2+"679811e2f503e03596dc3cda_2148682984.jpg", "qa", "4", "Discover leading organizations fighting for animal rights in California, from the Animal Legal Defense Fund to local shelters. Learn how you can support legal advocacy, protect animals, and make a difference. Request a free consultation today to explore your legal options for animal protection and advocacy."),
}
print("build.py loaded", len(PA), "practice areas,", len(BLOG), "posts")
