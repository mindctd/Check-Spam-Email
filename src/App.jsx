import React from "react";
import "./App.css";

export default function App() {
  return (
    <div className="font-inknut">
      
      {/* --- Top Section*/}
      <section className="GridWrapper">
        {/* Top Left Box */}
        <div className="Topleftbox">
          <h1 className="font-serif Textdetectmachine">DETECT MACHINE</h1>
        </div>

        {/* Top Right Box */}
        <div className="Toprightbox">
          <div className="flex items-center gap-3">
            <img
              src="/src/components/IMG_1893.png"
              className="w-12 h-12 object-contain"
              alt="Xspam Logo"
            />
            <h1 className="text-4xl text-white">
             <span className="font-serif TextXspam1 text-black">X</span><h className="font-serif TextXspam2">spam</h>
            </h1>
            </div>
        </div>

        {/* Bottom Left Box */}
        <div className="Bottomleftbox">
          <h1 className="font-serif flex items-start justify-start gap-4">What is Xspam </h1>
          <p className="font-serif text-sm max-w-xs mb-4">
            Xspam is detect machine to detect scammer and spam message.
          </p>
          <ul className="font-serif text-xs space-y-1">
            <li>• AI-based detection</li>
            <li>• Learns from history</li>
            <li>• Supports many languages</li>
            <li>• Browser integration</li>
          </ul>
          <div className="Robotpic">
          <img
              src="src\components\robotpic.png"
              className="w-80 h-80 object-contain"
              alt="robot"
            />
            </div>
        </div>
        
        {/* Bottom Right Box */}
        <div className="Bottomrightboxbg">
        <div className="Bottomrightbox">
          <h1 className="font-serif text-xl mb-2">What can Xspam do </h1>
          <p className="font-serif text-sm max-w-xs mb-4">
            Xspam removes toxic words and detects spamming users.
          </p>
          <ul className="font-serif text-xs space-y-1">
            <li>• Remove toxic words</li>
            <li>• Learn from chat history</li>
            <li>• Detects spam</li>
            <li>• Report abuse</li>
          </ul>
          </div>
          <div className="Bookpic">
          <img
              src="src\components\bookpic.png"
              className="w-80 h-80 object-contain"
              alt="book"
            />
            </div>
        </div>
      </section>

      {/* --- Middle Section (Download) --- */}
      <section className="bg-[#e75d5d] py-12 px-4 flex flex-col h-[450px]">
        <h2 className="font-serif text-white text-2xl mb-6">DOWNLOAD</h2>
      </section>

      {/* --- Footer Section --- */}
      <footer className="bg-[#2f2626] text-white py-10 px-6">
        <div className="flex flex-col md:flex-row justify-between items-center text-sm">
          <div className="mb-6 md:mb-0">
            <h3 className="font-bold text-lg mb-2">TULPAR</h3>
            <p>©Xspam AI 2025</p>
          </div>

          <div className="mb-6 md:mb-0">
            <h4 className="font-semibold mb-1">Pages</h4>
            <ul>
              <li>Home</li>
              <li>About</li>
              <li>Contact</li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-1">Connect with us</h4>
            <div className="flex gap-4">
              <span>🔴</span>
              <span>🔵</span>
              <span>⚪</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}




