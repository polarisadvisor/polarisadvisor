---
layout: base.njk
title: Contact
description: Start a measurement conversation with Polaris Advisor. Let's discuss how custom measurement design can help your organization.
---

<section class="contact-intro">
  <div class="container">
    <h1>Start a measurement conversation</h1>

    <div class="contact-header">
      <div class="advisor-profile">
        <img src="{{ '/assets/images/krishna-kumar.jpg' | url }}" alt="Krishna Kumar" class="advisor-photo">
        <div class="advisor-info">
          <h2>Krishna Kumar</h2>
          <p class="advisor-title">The Polaris Advisor Program</p>
          <p>I work with organizations to design measurement systems grounded in how their delivery process actually operates. If you're dissatisfied with off-the-shelf metrics and believe context matters, let's talk.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="contact-form-section">
  <div class="container-narrow">
    <h2>Get in touch</h2>
    <p>Describe your measurement challenge and we'll start a conversation about how Polaris can help.</p>

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
        <label for="challenge">What measurement challenges are you facing?</label>
        <textarea id="challenge" name="challenge" rows="6" required></textarea>
      </div>

      <div class="form-group">
        <label class="checkbox-label">
          <input type="checkbox" name="tried-dashboards" value="yes">
          I've tried existing metrics/dashboards and found them lacking
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
