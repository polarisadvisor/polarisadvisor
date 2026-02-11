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
              <svg class="icon" aria-hidden="true" focusable="false">
                <use href="{{ '/assets/icons/sprite.svg#icon-linkedin' | url }}"></use>
              </svg>
            </a>
            <a href="https://github.com/krishnaku" target="_blank" rel="noopener" aria-label="GitHub profile">
              <svg class="icon" aria-hidden="true" focusable="false">
                <use href="{{ '/assets/icons/sprite.svg#icon-github' | url }}"></use>
              </svg>
            </a>
          </div>
        </div>
        <div class="advisor-info">
          <h2>Dr. Krishna Kumar</h2>
          <p class="advisor-title">The Polaris Advisor Program</p>
          <p>I help leaders accountable for business outcomes design measurement systems that drive operational improvements across sales, product, engineering, and operations.</p>
          <p>My approach is useful if you're familiar with metrics in mainstream approaches— Lean/Agile/Kanban, DORA, SPACE, ToC, VSM, DevOps—and find they don't help you make clear decisions. My methods also work if your processes are homegrown and you lack a coherent measurement strategy. 
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
