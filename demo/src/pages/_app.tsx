import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import Script from 'next/script'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Script src='https://scripts.simpleanalyticscdn.com/latest.js' />
      <noscript>
        {/* eslint-disable @next/next/no-img-element */}
        <img src='https://queue.simpleanalyticscdn.com/noscript.gif' alt='' referrerPolicy='no-referrer-when-downgrade' />
      </noscript>
      <Component {...pageProps} />
    </>
  )
}
