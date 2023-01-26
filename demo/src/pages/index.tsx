import Head from 'next/head'
import styles from '@/styles/Home.module.css'
import Button from '@/components/Button'
import { useState } from 'react'
import { hwalja } from '@/data/hwalja'

const type = (past_state: string, hwalja_map: any, pressed: string, isEditing: boolean) => {
  const last_char = past_state.slice(-1)
  const last_two_char = past_state.slice(-2)
  if (isEditing && last_two_char in hwalja_map[pressed]) return past_state.slice(0, -2) + hwalja_map[pressed][last_two_char]
  if (isEditing && last_char in hwalja_map[pressed]) return past_state.slice(0, -1) + hwalja_map[pressed][last_char]
  return past_state + hwalja_map[pressed]['']
}

const ipsum = () => {
  const ipsums = [
    '죽는 날까지 하늘을 우러러',
    '한 점 부끄럼이 없기를',
    '잎새에 이는 바람에도',
    '나는 괴로워했다.',
    '별을 노래하는 마음으로',
    '모든 죽어 가는 것을 사랑해야지',
    '그리고 나한테 주어진 길을 걸어가야겠다.',
    '오늘 밤에도 별이 바람에 스치운다.',
  ]
  return ipsums[Math.floor(Math.random() * ipsums.length)]
}

export default function Home() {
  const [state, changeState] = useState(ipsum())
  const [isEditing, setIsEditing] = useState(false)
  return (
    <>
      <Head>
        <title>활자: 세상에서 가장 단순한 천지인 구현체</title>
        <meta name='description' content='활자: 세상에서 가장 단순한 천지인 구현체' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main className={styles.main}>
        <div className={styles.formbox} placeholder='무슨 생각을 하고 계신가요?'>
          {state}
        </div>
        <div className={styles.keypad}>
          <Button
            label='ㅣ'
            action={() => {
              changeState(type(state, hwalja, '인', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ᆞ'
            action={() => {
              changeState(type(state, hwalja, '천', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㅡ'
            action={() => {
              changeState(type(state, hwalja, '지', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㄱㅋ'
            action={() => {
              changeState(type(state, hwalja, 'ㄱㅋ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㄴㄹ'
            action={() => {
              changeState(type(state, hwalja, 'ㄴㄹ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㄷㅌ'
            action={() => {
              changeState(type(state, hwalja, 'ㄷㅌ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㅂㅍ'
            action={() => {
              changeState(type(state, hwalja, 'ㅂㅍ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㅅㅎ'
            action={() => {
              changeState(type(state, hwalja, 'ㅅㅎ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='ㅈㅎ'
            action={() => {
              changeState(type(state, hwalja, 'ㅈㅊ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='←'
            action={() => {
              changeState(state.slice(0, -1))
            }}
          />
          <Button
            label='ㅇㅁ'
            action={() => {
              changeState(type(state, hwalja, 'ㅇㅁ', isEditing))
              setIsEditing(true)
            }}
          />
          <Button
            label='_'
            action={() => {
              if (isEditing) {
                setIsEditing(false)
              } else {
                changeState(state + ' ')
              }
            }}
          />
        </div>
      </main>
    </>
  )
}
