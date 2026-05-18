# initWasm.js

Source: junk_drawer/github/EvolutionSimSite/src/wasm/initWasm.js.txt

Category: [[github-code]]

## Summary
// Initialize the Emscripten module export async function initWasm() { const Module = { print: (text) => console.log(text), printErr: (text) => console.error(text), canvas: (() => { const canvas = document.getElementById('canvas'); if (!canvas) { console.error('Canvas element not found'); return null;

## Full Content
// Initialize the Emscripten module
export async function initWasm() {
  const Module = {
    print: (text) => console.log(text),
    printErr: (text) => console.error(text),
    canvas: (() => {
      const canvas = document.getElementById('canvas');
      if (!canvas) {
        console.error('Canvas element not found');
        return null;
      }
      return canvas;
    })(),
    onRuntimeInitialized: () => {
      console.log('WebAssembly module initialized');
      // Dispatch a custom event when WebAssembly is ready
      window.dispatchEvent(new Event('wasm-initialized'));
    },
    locateFile: (path, prefix) => {
      // Adjust the path as needed for your setup
      return `/wasm/${path}`;
    },
    wasmMemory: new WebAssembly.Memory({ initial: 256, maximum: 65536 }),
    wasmTable: new WebAssembly.Table({ initial: 0, maximum: 10000, element: 'anyfunc' })
  };

  // Make Module available globally
  window.Module = Module;
  
  try {
    // The actual WebAssembly loading will be handled by Emscripten's generated code
    // We just need to make sure the Module object is available globally
    return Module;
  } catch (error) {
    console.error('Failed to initialize WebAssembly module:', error);
    throw error;
  }
}


## Metadata
- Source file: junk_drawer/github/EvolutionSimSite/src/wasm/initWasm.js.txt
- Extracted: 2026-05-18
- Category: github-code
