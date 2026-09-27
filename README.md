# MathCrypt-A-Multi-Algorithm-Password-Encryption-System-
it is an application that coverts password into encrypted message by using various operations like prime number, factors, etc.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Number DNA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0b1210; --panel:#111b17; --panel2:#0e1613;
    --border:#22322b; --text:#d9e8e0; --muted:#7d9a8c;
    --accent:#5fe3a3; --accent-dim:#2f6b52; --warn:#f2b134;
    box-sizing:border-box;
    padding-top:env(safe-area-inset-top,0px);
    padding-bottom:env(safe-area-inset-bottom,0px);
  }
  html{scroll-padding-top:env(safe-area-inset-top,0px);}
  *,*::before,*::after{box-sizing:inherit;}
  @media (prefers-color-scheme: light){
    :root:not([data-theme="dark"]){
      --bg:#f3f6f4; --panel:#ffffff; --panel2:#eef2f0;
      --border:#d3ddd8; --text:#12211b; --muted:#5a6f66;
      --accent:#178a56; --accent-dim:#cfe9dd; --warn:#a5680b;
    }
  }
  :root[data-theme="light"]{
    --bg:#f3f6f4; --panel:#ffffff; --panel2:#eef2f0;
    --border:#d3ddd8; --text:#12211b; --muted:#5a6f66;
    --accent:#178a56; --accent-dim:#cfe9dd; --warn:#a5680b;
  }
  body{
    margin:0; min-height:100%; background:var(--bg); color:var(--text);
    font-family:"IBM Plex Mono",ui-monospace,monospace;
    padding:28px 18px 48px;
  }
  .wrap{max-width:640px; margin:0 auto;}
  h1{
    font-size:1.15rem; font-weight:700; letter-spacing:.02em; margin:0 0 2px;
  }
  .sub{color:var(--muted); font-size:.82rem; margin:0 0 22px;}
  .tabs{display:flex; gap:2px; border:1px solid var(--border); border-radius:8px; padding:3px; margin-bottom:16px;}
  .tab{
    flex:1; padding:8px 10px; text-align:center; font-size:.82rem; cursor:pointer;
    border-radius:6px; color:var(--muted); user-select:none;
  }
  .tab.active{background:var(--accent-dim); color:var(--text); font-weight:600;}
  .panel{
    background:var(--panel); border:1px solid var(--border); border-radius:10px;
    padding:18px; margin-bottom:14px;
  }
  label{display:block; font-size:.75rem; color:var(--muted); margin-bottom:6px;}
  input[type=text]{
    width:100%; background:var(--panel2); border:1px solid var(--border); color:var(--text);
    font-family:inherit; font-size:.95rem; padding:10px 11px; border-radius:7px; outline:none;
  }
  input[type=text]:focus{border-color:var(--accent);}
  .row{display:flex; gap:8px; margin-top:12px;}
  button{
    font-family:inherit; font-size:.82rem; font-weight:600; cursor:pointer;
    border-radius:7px; padding:9px 14px; border:1px solid var(--border);
    background:var(--panel2); color:var(--text);
  }
  button.primary{background:var(--accent); border-color:var(--accent); color:#04150d;}
  button:focus-visible{outline:2px solid var(--accent); outline-offset:2px;}
  .readout{
    margin-top:16px; background:var(--panel2); border:1px solid var(--border); border-radius:8px;
    padding:14px 16px; font-size:.82rem; line-height:1.65; white-space:pre-wrap; word-break:break-word;
    overflow-x:auto;
  }
  .readout .k{color:var(--muted);}
  .readout .v{color:var(--text); font-weight:600;}
  .dna-line{color:var(--accent); font-weight:700; margin-top:8px; display:block; word-break:break-all;}
  .out-box{
    margin-top:14px; background:var(--panel2); border:1px dashed var(--border); border-radius:8px;
    padding:12px 14px; font-size:.78rem; word-break:break-all; color:var(--accent); min-height:20px;
  }
  .copy{margin-top:8px;}
  .hint{color:var(--muted); font-size:.72rem; margin-top:6px;}
  .err{color:var(--warn); font-size:.78rem; margin-top:8px;}
</style>
</head>
<body>
<div class="wrap">
  <h1>NUMBER DNA</h1>
  <p class="sub">every number has a profile — turn a password into its genetic readout</p>

  <div class="tabs">
    <div class="tab active" data-tab="profile">Number Profile</div>
    <div class="tab" data-tab="crypt">Password Encryptor</div>
  </div>

  <!-- PROFILE PANEL -->
  <div class="panel" id="panel-profile">
    <label for="numIn">Enter a whole number</label>
    <input type="text" id="numIn" placeholder="e.g. 84" inputmode="numeric">
    <div class="row"><button class="primary" id="profileBtn">Sequence it</button></div>
    <div id="profileOut"></div>
  </div>

  <!-- ENCRYPTOR PANEL -->
  <div class="panel" id="panel-crypt" style="display:none">
    <label for="pwIn">Password / text to encrypt</label>
    <input type="text" id="pwIn" placeholder="e.g. Tr0ub4dor">
    <div class="row">
      <button class="primary" id="encBtn">Encrypt to DNA</button>
    </div>
    <div class="out-box" id="encOut"></div>
    <div class="copy"><button id="copyBtn" style="display:none">Copy sequence</button></div>

    <label style="margin-top:18px" for="dnaIn">DNA sequence to decrypt</label>
    <input type="text" id="dnaIn" placeholder="paste an encrypted sequence">
    <div class="row"><button id="decBtn">Decrypt to text</button></div>
    <div class="out-box" id="decOut"></div>
    <div class="err" id="decErr"></div>
    <p class="hint">Each character is stored losslessly in its R (reverse) field — the rest of the profile is genuine number trivia, not needed to decode.</p>
  </div>
</div>

<script>
function isPrime(n){
  if(n<2) return false;
  if(n%2===0) return n===2;
  for(let i=3;i*i<=n;i+=2) if(n%i===0) return false;
  return true;
}
function factorCount(n){
  n=Math.abs(n); if(n===0) return Infinity;
  let c=0;
  for(let i=1;i*i<=n;i++){ if(n%i===0){ c+= (i*i===n)?1:2; } }
  return c;
}
function primeFactors(n){
  n=Math.abs(n); const out=[];
  let d=2;
  while(d*d<=n){ while(n%d===0){ out.push(d); n/=d; } d++; }
  if(n>1) out.push(n);
  return out.length?out:[n];
}
function digitSum(n){
  return String(Math.abs(n)).split('').reduce((a,c)=>a+Number(c),0);
}
function reverseDigits(str){ return str.split('').reverse().join(''); }
function gcd(a,b){ a=Math.abs(a); b=Math.abs(b); while(b){ [a,b]=[b,a%b]; } return a; }
function isPerfectSquare(x){ if(x<0) return false; const r=Math.round(Math.sqrt(x)); return r*r===x; }
function isFibonacci(n){ n=Math.abs(n); return isPerfectSquare(5*n*n+4)||isPerfectSquare(5*n*n-4); }

function profileOf(n){
  const p = isPrime(n);
  const fc = factorCount(n);
  const pf = primeFactors(n);
  const even = n%2===0;
  const ds = digitSum(n);
  const rev = reverseDigits(String(Math.abs(n)));
  const g = gcd(n,100);
  const fib = isFibonacci(n);
  const dna = `${even?'E':'O'}-F${fc}-P${pf.join('')}-S${ds}-R${rev}`;
  return {p,fc,pf,even,ds,rev,g,fib,dna};
}

function renderProfile(n){
  const pr = profileOf(n);
  return `<div class="readout">`+
    `<span class="k">NUMBER          </span><span class="v">${n}</span>\n`+
    `<span class="k">Prime?          </span><span class="v">${pr.p?'YES':'NO'}</span>\n`+
    `<span class="k">Factors         </span><span class="v">${pr.fc}</span>\n`+
    `<span class="k">Prime Factors   </span><span class="v">${pr.pf.join(',')}</span>\n`+
    `<span class="k">Even/Odd        </span><span class="v">${pr.even?'EVEN':'ODD'}</span>\n`+
    `<span class="k">Digit Sum       </span><span class="v">${pr.ds}</span>\n`+
    `<span class="k">Reverse         </span><span class="v">${pr.rev}</span>\n`+
    `<span class="k">GCD with 100    </span><span class="v">${pr.g}</span>\n`+
    `<span class="k">Fibonacci?      </span><span class="v">${pr.fib?'YES':'NO'}</span>\n`+
    `<span class="dna-line">DNA: ${pr.dna}</span>`+
    `</div>`;
}

// ---- tabs ----
document.querySelectorAll('.tab').forEach(t=>{
  t.addEventListener('click',()=>{
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
    t.classList.add('active');
    const which = t.dataset.tab;
    document.getElementById('panel-profile').style.display = which==='profile'?'block':'none';
    document.getElementById('panel-crypt').style.display = which==='crypt'?'block':'none';
  });
});

// ---- profile ----
document.getElementById('profileBtn').addEventListener('click', ()=>{
  const raw = document.getElementById('numIn').value.trim();
  const out = document.getElementById('profileOut');
  if(!/^-?\d+$/.test(raw)){ out.innerHTML = `<div class="err">Enter a whole number.</div>`; return; }
  out.innerHTML = renderProfile(parseInt(raw,10));
});
document.getElementById('numIn').addEventListener('keydown', e=>{ if(e.key==='Enter') document.getElementById('profileBtn').click(); });

// ---- encrypt: each char -> 3-digit zero-padded code -> DNA block, R field carries the reversible payload ----
function encryptText(str){
  const blocks = [];
  for(const ch of str){
    const code = ch.codePointAt(0);
    const padded = String(code).padStart(3,'0');
    const revPadded = reverseDigits(padded);
    const pr = profileOf(code);
    blocks.push(`${pr.even?'E':'O'}-F${pr.fc}-P${pr.pf.join('')}-S${pr.ds}-R${revPadded}`);
  }
  return blocks.join('|');
}
function decryptDna(seq){
  const blocks = seq.split('|').filter(Boolean);
  let out = '';
  for(const b of blocks){
    const m = b.match(/-R(\d+)$/);
    if(!m) throw new Error(`Malformed block: "${b}"`);
    const padded = reverseDigits(m[1]).padStart(3,'0');
    out += String.fromCodePoint(parseInt(padded,10));
  }
  return out;
}

document.getElementById('encBtn').addEventListener('click', ()=>{
  const val = document.getElementById('pwIn').value;
  const outBox = document.getElementById('encOut');
  const copyBtn = document.getElementById('copyBtn');
  if(!val){ outBox.textContent=''; copyBtn.style.display='none'; return; }
  const enc = encryptText(val);
  outBox.textContent = enc;
  copyBtn.style.display = 'inline-block';
  copyBtn.onclick = async ()=>{
    try{ await navigator.clipboard.writeText(enc); copyBtn.textContent='Copied!'; setTimeout(()=>copyBtn.textContent='Copy sequence',1200); }
    catch(e){ copyBtn.textContent='Select & copy manually'; }
  };
});

document.getElementById('decBtn').addEventListener('click', ()=>{
  const seq = document.getElementById('dnaIn').value.trim();
  const outBox = document.getElementById('decOut');
  const errBox = document.getElementById('decErr');
  errBox.textContent=''; outBox.textContent='';
  if(!seq) return;
  try{ outBox.textContent = decryptDna(seq); }
  catch(e){ errBox.textContent = 'Could not decode — check the sequence was copied in full.'; }
});
</script>
</body>
</html>
