import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.doupocangqiong.org/doupocangqiong/');
  await page.getByRole('link', { name: '开始阅读' }).click();
  await page.getByRole('link', { name: '下一章' }).click();
  await page.getByRole('link', { name: '下一章' }).click();
  await page.getByRole('link', { name: '下一章' }).click();
});