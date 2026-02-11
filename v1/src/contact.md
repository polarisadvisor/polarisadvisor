---
layout: base.njk
title: Contact
description: Start a measurement conversation with Polaris Advisor. Let's discuss how custom measurement design can help your organization.
---

<section class="contact-intro">
  <div class="container">
    <h1>Let's Talk</h1>

    <div class="contact-header">
      <div class="advisor-profile">
        <div class="advisor-photo-container">
          <img src="{{ '/assets/images/krishna-kumar.jpg' | url }}" alt="Krishna Kumar" class="advisor-photo">
          <div class="social-badges">
            <a href="https://www.linkedin.com/in/krishnaku1/" target="_blank" rel="noopener" aria-label="LinkedIn profile">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>
            </a>
            <a href="https://github.com/krishnaku" target="_blank" rel="noopener" aria-label="GitHub profile">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
          </div>
        </div>
        <div class="advisor-info">
          <h2>Dr. Krishna Kumar</h2>
          <p class="advisor-title">The Polaris Advisor Program</p>
          <p>I help leaders accountable for business outcomes design measurement systems that drive operational improvements across sales, product, engineering, and operations.</p>
          <p>My approach is useful if you're familiar with metrics in mainstream approaches— Lean/Agile/Kanban, DORA, SPACE, ToC, VSM, DevOps—and find they dont help you make clear decisions. They also work if your processes are homegrown and you lack a coherent measurement strategy. 
            </p>
            <p>
            My methods rethink <em>measurement</em> from first principles, so they work in both cases.
            If simpler metrics from mainstream approaches satisfy your needs, I may not add value.</p>

        </div>
      </div>
    </div>
  </div>
</section>

<section class="qualifier">
  <div class="container-narrow">
    <h2>Are we a fit?</h2>
    <p>If you believe context matters—that your organization is unique and needs a measurement system that reflects that—we should talk.</p>

    <h3>I am not the right fit if you want:</h3>
    <ul>
      <li>An install-a-dashboard solution</li>
      <li>Simplistic productivity metrics</li>
      <li>Someone to implement the latest buzzword-compliant metrics framework</li>
      <li>Someone to help you adopt generic industry benchmarks or scorecards</li>
      <li>Instant answers without deeply engaging the system to understand how it works</li>
    </ul>
  </div>
</section>

<section class="contact-form-section">
  <div class="container-narrow">
    <h2>Tell me a bit about you</h2>
    <form class="contact-form" action="https://formspree.io/f/xnjbqkkr" method="POST">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required>
      </div>

      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
      </div>

      <div class="form-group">
        <label for="organization">Organization</label>
        <input type="text" id="organization" name="organization">
      </div>

      <div class="form-group">
        <label for="website">Company website</label>
        <input type="url" id="website" name="website" placeholder="https://">
      </div>

      <div class="form-group">
        <label for="challenge">What pain points are you facing with your operational metrics today?</label>
        <textarea id="challenge" name="challenge" rows="6" required></textarea>
      </div>

      <div class="form-group">
        <label class="checkbox-label">
          <input type="checkbox" name="tried-dashboards" value="yes">
          I've improved operations but my measurements don't show it
        </label>
      </div>

      <button type="submit" class="btn btn-primary">Send message</button>
    </form>
  </div>
</section>

<section class="secondary-ctas">
  <div class="container">
    <h3>Explore first?</h3>
    <div class="cta-links">
      <a href="{{ site.dispatch.url }}" target="_blank" rel="noopener">Read The Polaris Flow Dispatch</a>
      <a href="{{ site.github.docs }}" target="_blank" rel="noopener">Review The Presence Calculus</a>
      <a href="{{ site.github.opensource }}" target="_blank" rel="noopener">Explore open-source tools</a>
    </div>
  </div>
</section>
