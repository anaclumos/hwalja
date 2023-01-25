import React, { MouseEventHandler } from 'react'
import styles from '@/styles/Home.module.css'

type Props = {
  label: string
  action?: MouseEventHandler<HTMLButtonElement>
}

const Button = ({ label, action }: Props) => {
  return (
    <button className={styles.key} onClick={action}>
      {label}
    </button>
  )
}

export default Button
