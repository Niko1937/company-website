LABELS = {'nav': 'Site', 'home': 'Home', 'toc': 'Contents', 'legal': 'Legal', 'privacy': 'Privacy Policy', 'terms': 'Terms of Use', 'contact': 'Contact'}
# No email address is shown on the site (spam). Requests go through the contact form on the home page.
FORM = '<a href="/en/#contact">our contact form</a>'
ADDRESS = '68 Circular Road, #02-01, Singapore 049422'

PRIVACY = {
'labels': LABELS,
'title': 'Privacy Policy',
'description': 'How Quests Bay Pte. Ltd. collects, uses and protects personal data.',
'updated': 'Last updated: October 26, 2026',
'lead': 'This Privacy Policy explains how Quests Bay Pte. Ltd. (“Quests”, “we”, “us”) collects, uses, discloses and protects personal data when you visit this website, contact us, or work with us. It is written to meet the Personal Data Protection Act 2012 of Singapore (PDPA) and, for people in Japan, the Act on the Protection of Personal Information (APPI).',
'sections': [
('who-we-are', '1. Who we are', f'''<p>Quests Bay Pte. Ltd. is a company incorporated in Singapore and is responsible for the personal data described in this policy.</p>
<ul><li>Address: {ADDRESS}</li><li>Contact: {FORM}</li></ul>
<p>The name of our representative director is available on request.</p>'''),
('data-we-collect', '2. Personal data we collect', '''<h3>When you contact us</h3>
<p>Our contact form does not send your details to our servers. It opens your own email app or service with a message addressed to us. We receive only what you choose to send, typically your name, email address, company name, budget range and the details of your project, plus anything else you include in your email.</p>
<h3>When we work with you</h3>
<p>If you or your organisation become a client, partner or supplier, we collect business contact details (such as name, job title, company, email address and phone number) and the information needed to deliver and manage the engagement.</p>
<h3>When you visit this website</h3>
<p>Like most websites, the services that host and support this site automatically receive technical data such as your IP address, browser type, device information, the pages you request and the date and time. We do not use analytics tools, advertising cookies or tracking pixels on this website.</p>
<h3>Personal data we handle for our clients</h3>
<p>In client projects, we may handle personal data on a client’s behalf, such as data about the client’s customers or employees. We handle it only on the client’s instructions and under our agreement with that client. That processing is governed by the agreement and the client’s own privacy notice, not by this policy.</p>'''),
('how-we-use', '3. How we use personal data', '''<p>We use personal data for these purposes:</p>
<ul>
<li>To respond to your enquiries and arrange meetings</li>
<li>To prepare proposals, enter into contracts and deliver our services</li>
<li>To manage our relationship with clients, partners and suppliers, including billing</li>
<li>To send information about our services when you have asked for it (you can opt out at any time)</li>
<li>To keep this website and our systems secure and working properly</li>
<li>To meet legal, regulatory and accounting obligations, and to establish or defend legal claims</li>
</ul>
<p>We will not use personal data for a new purpose without telling you and, where required, obtaining your consent.</p>'''),
('cookies', '4. Cookies and browser storage', '''<p>This website does not set its own cookies. It stores your chosen language in your browser (local storage) so the site opens in that language next time, and briefly uses session storage to load updated content. Neither is used to identify or track you, and you can clear them at any time in your browser settings.</p>
<p>Some third-party services shown on this site may set their own cookies, as described in the next section.</p>'''),
('third-party-services', '5. Third-party services on this website', '''<p>This website uses the following services. When your browser connects to them, they may receive technical data such as your IP address and browser information, and they handle it under their own privacy policies.</p>
<div class="table-wrap"><table>
<thead><tr><th>Service</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>GitHub Pages (GitHub, Inc.)</td><td>Hosting this website</td></tr>
<tr><td>Google Maps (Google LLC)</td><td>Showing our office location in the contact section</td></tr>
<tr><td>YouTube (Google LLC)</td><td>Playing solution demo videos. Videos load only after you choose to play one, in YouTube’s privacy-enhanced mode. Thumbnails are loaded from YouTube’s image server.</td></tr>
<tr><td>Google Fonts (Google LLC)</td><td>Displaying fonts</td></tr>
<tr><td>cdnjs (Cloudflare, Inc.), jsDelivr, Tailwind CSS CDN</td><td>Delivering the scripts and styles this site uses</td></tr>
<tr><td>Gmail, Outlook or your own email app</td><td>Sending your message, if you choose one of them in our contact form</td></tr>
</tbody></table></div>'''),
('sharing', '6. How we share personal data', '''<p>We do not sell personal data. We share it only as follows:</p>
<ul>
<li><strong>Service providers</strong> who help us run our business, such as email, cloud storage and accounting services, under contracts that require them to protect the data and use it only for our purposes</li>
<li><strong>Professional advisers</strong> such as lawyers, auditors and insurers, under duties of confidentiality</li>
<li><strong>Authorities</strong> when required by law, regulation or court order</li>
<li><strong>A buyer or successor</strong> if our business is reorganised, merged or sold, subject to this policy</li>
<li><strong>Anyone else</strong> with your consent</li>
</ul>'''),
('international-transfers', '7. International transfers', '''<p>We are based in Singapore, and our service providers may store or process personal data in other countries, including the United States. When we transfer personal data outside Singapore, we take steps to ensure it receives a standard of protection comparable to the PDPA, for example through contractual commitments.</p>
<p>For people in Japan: when we provide personal data to a third party in a foreign country, we do so in line with the APPI. On request, we will provide information about the country concerned, its personal information protection system and the measures the recipient takes.</p>'''),
('security', '8. How we protect personal data', '''<p>We use reasonable organisational and technical measures to protect personal data against unauthorised access, use, loss or disclosure. These include limiting access to people who need it, requiring confidentiality from staff and contractors, using reputable service providers with strong security, and encrypting data in transit where appropriate.</p>
<p>Where we store personal data with providers in other countries, we do so after checking the personal data protection systems of those countries.</p>
<p>No method of transmission over the internet is completely secure. Please do not send highly sensitive or confidential information through ordinary email until we have agreed how to exchange it.</p>'''),
('retention', '9. How long we keep personal data', '''<p>We keep personal data only for as long as it is needed for the purposes described in this policy, or as required by law (for example, for tax and accounting records). When it is no longer needed, we delete it or make it anonymous.</p>'''),
('your-rights', '10. Your rights', f'''<p>Subject to applicable law, you can ask us to:</p>
<ul>
<li>Tell you what personal data we hold about you and how it has been used or disclosed</li>
<li>Correct personal data that is inaccurate or incomplete</li>
<li>Stop using or delete your personal data, or stop providing it to third parties</li>
<li>Withdraw consent you have given. We will tell you the likely consequences before acting on it.</li>
<li>Stop sending you information about our services</li>
</ul>
<p>To make a request, please contact us through {FORM}. We may need to verify your identity before we respond, and we will reply within a reasonable time. Where the law allows, we may charge a reasonable fee for access requests, and we will tell you the amount in advance.</p>'''),
('children', '11. Children', '''<p>This website and our services are intended for businesses and are not directed to children. We do not knowingly collect personal data from children.</p>'''),
('links', '12. Links to other websites', '''<p>This website may link to other websites, such as our YouTube channel. We are not responsible for the privacy practices of those websites, and we encourage you to read their privacy policies.</p>'''),
('changes', '13. Changes to this policy', '''<p>We may update this policy from time to time. We will post the updated version on this page with a new “Last updated” date. If the changes are significant, we will take reasonable steps to let you know.</p>'''),
('contact', '14. Contact us', f'''<p>For questions, requests or complaints about this policy or our handling of personal data, please contact our Data Protection Officer.</p>
<div class="contact"><p><strong>Data Protection Officer, Quests Bay Pte. Ltd.</strong><br>{ADDRESS}<br>Contact: {FORM}</p></div>'''),
],
}

TERMS = {
'labels': LABELS,
'title': 'Terms of Use',
'description': 'The terms that apply when you use the Quests website.',
'updated': 'Last updated: October 26, 2026',
'lead': 'These Terms of Use apply to your use of this website, operated by Quests Bay Pte. Ltd. (“Quests”, “we”, “us”). By using the website, you agree to these terms. If you do not agree, please do not use it.',
'sections': [
('about-site', '1. About this website', '''<p>This website provides general information about Quests and our services. It is not professional advice, and you should not rely on it as such. Any services we provide are governed by a separate written agreement between you and us.</p>
<p>Case studies describe past projects in general terms. Results depend on each client’s circumstances and are not a guarantee of future results.</p>'''),
('intellectual-property', '2. Intellectual property', '''<p>The content of this website, including text, images, videos, graphics and logos, is owned by Quests or our licensors and is protected by copyright and other laws. You may view it and print or save individual pages for your own non-commercial use, provided you keep all copyright and other notices. Any other use requires our prior written permission.</p>
<p>Other company names, product names and logos on this website are the trademarks of their respective owners. Their appearance does not imply any endorsement or partnership unless we say so.</p>'''),
('acceptable-use', '3. Acceptable use', '''<p>You agree not to:</p>
<ul>
<li>Use the website in any way that is unlawful or infringes the rights of others</li>
<li>Try to gain unauthorised access to the website or the systems that support it, or interfere with how they work</li>
<li>Introduce viruses or other harmful code</li>
<li>Collect data from the website by automated means in a way that places an unreasonable load on it</li>
<li>Send us false or misleading information, or impersonate anyone else</li>
</ul>'''),
('information-you-send', '4. Information you send us', '''<p>Please do not send confidential or proprietary information through the contact form or by email before we have agreed in writing how it will be handled, such as through a non-disclosure agreement. Unless we have agreed otherwise, ideas or suggestions you send us are not treated as confidential, and we may use them without obligation to you.</p>
<p>We handle personal data you send us in line with our <a href="../privacy/">Privacy Policy</a>.</p>'''),
('third-party', '5. Third-party links and services', '''<p>This website includes links to, and content from, third-party websites and services such as YouTube and Google Maps. We do not control them and are not responsible for their content, availability or practices. Your use of them is subject to their own terms.</p>'''),
('disclaimer', '6. Disclaimer', '''<p>We aim to keep the website accurate and available, but it is provided “as is” and “as available”. To the fullest extent permitted by law, we make no warranties of any kind, express or implied, including about its accuracy, completeness, reliability, fitness for a particular purpose or freedom from errors, viruses or interruptions.</p>'''),
('liability', '7. Limitation of liability', '''<p>To the fullest extent permitted by law, Quests will not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of profits, data or business opportunity, arising from your use of, or inability to use, this website or its content. Nothing in these terms limits liability that cannot be limited under applicable law.</p>'''),
('changes', '8. Changes', '''<p>We may change the website or these terms at any time. The updated terms will be posted on this page with a new “Last updated” date, and they apply from the time they are posted.</p>'''),
('governing-law', '9. Governing law and jurisdiction', '''<p>These terms are governed by the laws of Singapore. The courts of Singapore have exclusive jurisdiction over any dispute arising from them or from your use of the website.</p>'''),
('general', '10. General', '''<p>If any part of these terms is found to be invalid or unenforceable, the rest remains in effect. Our failure to enforce any part of these terms is not a waiver of our right to do so later. If the English and Japanese versions of these terms differ, the English version prevails.</p>'''),
('contact', '11. Contact us', f'''<div class="contact"><p><strong>Quests Bay Pte. Ltd.</strong><br>{ADDRESS}<br>Contact: {FORM}</p></div>'''),
],
}
