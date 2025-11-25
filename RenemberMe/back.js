    window.addEventListener('DOMContentLoaded', () => {
      load();
    });

    const STORAGE_KEY = 'tablero_recordatorios_v1';
    let reminders = [];

    const el = id => document.getElementById(id);
    const $ = s => document.querySelector(s);

    function load() {
      const raw = localStorage.getItem(STORAGE_KEY);
      reminders = raw ? JSON.parse(raw) : [];
      render();
      scheduleAll();
    }

    function save() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(reminders));
      render();
    }

    function uid() { return 'id-' + Date.now() + '-' + Math.floor(Math.random()*9999); }

    function render() {
      const container = el('reminderList');
      container.innerHTML = '';
      const view = document.querySelector('#views .active')?.dataset.view || 'all';
      const q = el('searchInput').value.trim().toLowerCase();
      const priorityFilter = el('filterPriority').value;

      let list = reminders.slice();

      if (q) list = list.filter(r => (r.title + ' ' + (r.tag||'') + ' ' + (r.description||'')).toLowerCase().includes(q));
      if (priorityFilter !== 'all') list = list.filter(r => r.priority === priorityFilter);

      const now = new Date();
      if (view === 'today') {
        list = list.filter(r => isSameDay(new Date(r.when), now));
      } else if (view === 'upcoming') {
        const weekAhead = new Date(); weekAhead.setDate(now.getDate()+7);
        list = list.filter(r => new Date(r.when) >= now && new Date(r.when) <= weekAhead);
      } else if (view === 'missed') {
        list = list.filter(r => new Date(r.when) < now && !r.completed);
      }

      const sortBy = el('sortBy').value;
      if (sortBy === 'next') list.sort((a,b)=> new Date(a.when)-new Date(b.when));
      if (sortBy === 'priority') list.sort((a,b)=> priorityValue(b.priority)-priorityValue(a.priority));
      if (sortBy === 'date') list.sort((a,b)=> new Date(a.when)-new Date(b.when));

      el('count').innerText = list.length;

      if (!list.length) {
        container.innerHTML = '<div class="col-12"><div class="card p-4 text-center shadow-sm"><div class="fw-bold">Sin recordatorios</div><div class="small-muted">Crea uno nuevo para empezar — botón "Nuevo"</div></div></div>';
        return;
      }

      for (const r of list) {
        const when = new Date(r.when);
        const isPast = when < new Date();
        const card = document.createElement('div'); card.className = 'col-12 col-md-6';
        card.innerHTML = `
          <div class="card card-reminder ${r.priority} shadow-sm">
            <div class="card-body">
              <div class="d-flex justify-content-between align-items-start">
                <div>
                  <h5 class="card-title mb-1">${escapeHtml(r.title)}</h5>
                  <div class="small-muted mb-2">${r.tag ? escapeHtml(r.tag) + ' · ' : ''}${when.toLocaleString()}</div>
                </div>
                <div class="text-end">
                  <button class="btn btn-sm btn-outline-secondary me-1" data-id="${r.id}" data-action="edit"><i class="bi bi-pencil"></i></button>
                  <button class="btn btn-sm btn-outline-danger" data-id="${r.id}" data-action="delete"><i class="bi bi-trash"></i></button>
                </div>
              </div>
              <p class="card-text">${escapeHtml(r.description||'')}</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="small-muted">${r.repeat !== 'none' ? 'Repite: ' + r.repeat : ''}</div>
                <div>
                  ${isPast ? '<span class="badge bg-danger">Vencido</span>' : ''}
                  ${r.completed ? '<span class="badge bg-success">Completado</span>' : ''}
                </div>
              </div>
            </div>
          </div>
        `;
        container.appendChild(card);
      }

      container.querySelectorAll('button').forEach(btn=>{
        btn.addEventListener('click', e=>{
          const id = btn.dataset.id; const action = btn.dataset.action;
          if (action === 'edit') openEdit(id);
          if (action === 'delete') { if (confirm('Eliminar recordatorio?')) { deleteReminder(id); } }
        });
      });
    }

    function escapeHtml(s='') { return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;'); }

    function priorityValue(p){ return p==='high'?3: p==='medium'?2:1 }
    function isSameDay(a,b){ return a.getFullYear()===b.getFullYear() && a.getMonth()===b.getMonth() && a.getDate()===b.getDate(); }
    function addReminder(obj){ reminders.push(obj); save(); scheduleReminder(obj); }
    function updateReminder(id, patch){ const i = reminders.findIndex(r=>r.id===id); if (i>-1){ reminders[i] = {...reminders[i], ...patch}; save(); scheduleAll(); } }
    function deleteReminder(id){ reminders = reminders.filter(r=>r.id!==id); save(); }
    const modalEl = document.getElementById('reminderModal');
    const modal = new bootstrap.Modal(modalEl);

    document.getElementById('reminderForm').addEventListener('submit', e=>{
      e.preventDefault();
      const id = el('reminderId').value || uid();
      const title = el('title').value.trim();
      const description = el('description').value.trim();
      const tag = el('tag').value.trim();
      const priority = el('priority').value;
      const date = el('date').value;
      const time = el('time').value;
      const repeat = el('repeat').value;
      const lead = parseInt(el('leadMinutes').value || '0',10);
      const when = new Date(date + 'T' + time);

      const payload = { id, title, description, tag, priority, when: when.toISOString(), repeat, leadMinutes: lead, completed:false };
      const exists = reminders.find(r=>r.id===id);
      if (exists) updateReminder(id, payload); else addReminder(payload);
      modal.hide();
      e.target.reset();
    });
    function openEdit(id){ const r = reminders.find(x=>x.id===id); if (!r) return; el('modalTitle').innerText = 'Editar recordatorio'; el('reminderId').value = r.id; el('title').value=r.title; el('description').value=r.description||''; el('tag').value=r.tag||''; el('priority').value=r.priority||'medium'; const dt = new Date(r.when); el('date').value = dt.toISOString().slice(0,10); el('time').value = dt.toTimeString().slice(0,5); el('repeat').value = r.repeat||'none'; el('leadMinutes').value = r.leadMinutes||10; modal.show(); }
    document.querySelectorAll('#views button').forEach(b=> b.addEventListener('click', e=>{ document.querySelectorAll('#views button').forEach(x=>x.classList.remove('active')); e.currentTarget.classList.add('active'); render(); }));
    ['searchInput','filterPriority','sortBy'].forEach(id=> el(id).addEventListener('input', render));
    el('btnAdd').addEventListener('click', ()=>{ el('reminderForm').reset(); el('reminderId').value=''; el('modalTitle').innerText='Nuevo recordatorio'; });
    async function requestPermission(){ if (Notification.permission === 'default') await Notification.requestPermission(); }
    el('toggleNotifications').addEventListener('change', async (e)=>{ if (e.target.checked) await requestPermission(); });

    function scheduleReminder(r){ try{s
      if (r._timeout) clearTimeout(r._timeout);
      const when = new Date(r.when);
      const alarmAt = new Date(when.getTime() - ( (r.leadMinutes||0) * 60000 ));
      const ms = alarmAt - new Date();
      if (ms <= 0) return; 
      r._timeout = setTimeout(()=> triggerAlarm(r), ms);
    }catch(e){ console.error(e); }
    }

    function scheduleAll(){
      reminders.forEach(r=>{ if (r._timeout) clearTimeout(r._timeout); });
      reminders.forEach(scheduleReminder);
    }

    function triggerAlarm(r){
      if (Notification.permission === 'granted' && el('toggleNotifications').checked){
        new Notification(r.title, { body: r.description || 'Recordatorio', tag: r.id });
      } else {
        showInAppToast(r.title, r.description);
      }
      if (r.emailNotify) console.log('Simular envío de correo para', r.id);
      if (r.repeat && r.repeat !== 'none'){
        const next = nextOccurrence(new Date(r.when), r.repeat);
        updateReminder(r.id, { when: next.toISOString() });
      }
    }

    function nextOccurrence(dt, rule){ const n = new Date(dt);
      if (rule === 'daily') n.setDate(n.getDate()+1);
      if (rule === 'weekly') n.setDate(n.getDate()+7);
      if (rule === 'monthly') n.setMonth(n.getMonth()+1);
      return n;
    }

    function showInAppToast(title, body){ const toast = document.createElement('div'); toast.className='toast align-items-center show position-fixed bottom-0 end-0 m-3'; toast.style.zIndex=9999; toast.innerHTML = `<div class="d-flex"><div class="toast-body"><strong>${escapeHtml(title)}</strong><div class="small-muted">${escapeHtml(body||'')}</div></div><button class="btn-close me-2 m-auto" onclick="this.parentNode.parentNode.remove()"></button></div>`; document.body.appendChild(toast); setTimeout(()=> toast.remove(), 10000); }
    function deleteAllScheduled(){ reminders.forEach(r=>{ if (r._timeout) clearTimeout(r._timeout); delete r._timeout; }); }
    if (!localStorage.getItem(STORAGE_KEY)){
      const sampleWhen = new Date(); sampleWhen.setMinutes(sampleWhen.getMinutes()+60);
      reminders = [{ id: uid(), title:'Reunión con equipo', description:'Revisión del avance del proyecto', tag:'Trabajo', priority:'medium', when: sampleWhen.toISOString(), repeat:'none', leadMinutes:15, completed:false }];
      save();
    }
    load();
    window._app = { reminders, load, save, addReminder, updateReminder, deleteReminder };